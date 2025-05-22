from pydantic import BaseModel, EmailStr
from typing import List, Optional, Literal

class NotificationRequest(BaseModel):
    user_id: Optional[str] = None
    email: Optional[List[EmailStr]] = None
    phone_number: Optional[List[str]] = None
    type: Literal["inapp", "email", "sms"]
    message: str