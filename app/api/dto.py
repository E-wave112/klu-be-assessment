from __future__ import annotations
from pydantic import BaseModel
from typing import Union


DataDict = dict[str, Union[bool, str, dict[str, str]]]
class ConversationInput(BaseModel):
    conversation: dict[str, str]

class ChatCompletionResponse(BaseModel):
    data: DataDict