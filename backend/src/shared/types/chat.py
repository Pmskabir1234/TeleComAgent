from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ChatMessageRequest(BaseModel):
    conversation_id: Optional[int] = None
    message: str

class MessageResponse(BaseModel):
    role: str
    content: str
    created_at: datetime

class ChatResponse(BaseModel):
    conversation_id: int
    messages: List[MessageResponse]
