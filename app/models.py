from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChatMessage(BaseModel):
    message: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    session_id: Optional[str] = None
    timestamp: str


class HealthResponse(BaseModel):
    status: str
    timestamp: str
