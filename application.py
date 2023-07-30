from fastapi import FastAPI
from app.api.main import conversation

app = FastAPI(openapi_url="/openapi.json")


app.router.prefix = "/api/v1"
app.include_router(conversation, prefix="/chat", tags=["conversation"])
