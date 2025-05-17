from pydantic import BaseModel
from typing import Literal

class NotificationRequest(BaseModel):
    user_id: str
    type: Literal["inapp"]
    message: str