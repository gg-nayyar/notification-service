from pydantic import BaseModel, EmailStr
from typing import Optional, Literal

class NotificationRequest(BaseModel):
    user_id: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    type: Literal["inapp", "email", "sms"]
    message: str