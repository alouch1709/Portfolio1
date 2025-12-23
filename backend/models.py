from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class ContactMessage(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=200)
    message: str = Field(..., min_length=10, max_length=2000)

class ContactMessageDB(ContactMessage):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    read: bool = False

class ContactResponse(BaseModel):
    success: bool
    message: str
    id: Optional[str] = None