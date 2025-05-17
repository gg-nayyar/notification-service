from datetime import datetime
from app.db import notification
from app.models import format_notification
from app.schemas import NotificationRequest
from fastapi import APIRouter, HTTPException

router = APIRouter()
@router.post("/notifications")
def create_notification(payload: NotificationRequest):
    doc = {
        "user_id": payload.user_id,
        "type": payload.type,
        "message": payload.message,
        "timestamp": datetime.utcnow(),
    }
    notification.insert_one(doc)
    return {"message": "Notification created successfully",
            "notification": format_notification(doc)}
    
@router.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: str):
    user_notifications = notification.find({"user_id": user_id})
    return [format_notification(notification) for notification in user_notifications]