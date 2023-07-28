from fastapi import APIRouter, Query

import time
import requests
import json
from typing import Optional

from app.api.dto import ConversationInput, ChatCompletionResponse
from app.utils.logger_file import get_logger_info

logger = get_logger_info(__name__)

conversation = APIRouter()


dataset = json.load(open("ShareGPT_V3_unfiltered_cleaned_split.json", "r"))


class ChatCompletionRequest(ConversationInput):
    pass


@conversation.post("/completion", response_model=ChatCompletionResponse)
def chat_completion(payload: ChatCompletionRequest):
    try:
        conversation_input = payload.conversation
        # Loop through the list of dictionaries
        for item in dataset:
            # Access the "conversations" list within each dictionary
            conversations = item.get("conversations", [])
            for i in range(len(conversations)):
                # Check if the current dictionary matches the input dictionary based on the "value" field
                if conversations[i].get("value") == conversation_input["value"]:
                    # Check if the next dictionary exists
                    if i + 1 < len(conversations):
                        # Return the next dictionary in the list
                        return {
                            "data": {"success": True, "response": conversations[i + 1]}
                        }

        # If no match is found or the match is the last dictionary in the list, return None
        return {"data": {"success": False, "errror": "Invalid conversation object"}}
    except Exception as e:
        raise e


@conversation.post("/completion/v1")
def chat_completion(payload: ChatCompletionRequest):
    try:
        conversation_input = payload.conversation

        # Define a generator function to yield the next dictionary following the match
        def next_dict_generator():
            for item in dataset:
                conversations = item.get("conversations", [])
                for i in range(len(conversations)):
                    if conversations[i].get("value") == conversation_input["value"]:
                        if i + 1 < len(conversations):
                            yield conversations[i + 1]

        # Create the generator object
        generator = next_dict_generator()
        response = next(generator, None)
        if not response:
            return {"data": {"success": False, "errror": "Invalid conversation object"}}

        # Use next() to get the first match (or None if no match)
        return {"data": {"success": True, "response": response}}
    except Exception as e:
        raise e


# Include the endpoint for latency measurement
@conversation.get("/api/benchmarks")
def latency_measurement(
    path: Optional[str] = Query(
        "/completion",
        max_length=100,
    ),
):
    base_url = "http://127.0.0.1:8000/api/v1/chat"
    total_requests = 100
    total_latency = 0
    for i in range(total_requests):
        start_time = time.time()
        requests.post(
            f"{base_url}{path}",
            json={
                "conversation": {
                    "from": "human",
                    "value": "Fill sample data in the following table:\nCompanyName Region District StoreName EmployeeName GroupCustomerId TrafficCount TotalInteractionTime",
                }
            },
        )
        latency = time.time() - start_time
        total_latency += latency

        avg_latency = total_latency / total_requests
        requests_per_minute = 60 / avg_latency

    logger.info(f"Requests per minute: {requests_per_minute:.2f}")
    logger.info(f"Average latency: {avg_latency:.6f} seconds")
    return {
        "requests_per_minute": f"{requests_per_minute:.2f}",
        "avg_latency_in_seconds": f"{avg_latency:.6f}",
    }
