from datetime import datetime
from app.db import notification
from app.models import format_notification
from app.schemas import NotificationRequest
from fastapi import APIRouter, HTTPException
from app.services.sms_service import send_sms
from app.services.email_service import send_email

router = APIRouter()
@router.post("/notifications")
def create_notification(payload: NotificationRequest):
    if payload.type == "inapp":
        if not payload.user_id:
            raise HTTPException(status_code=400, detail="user_id is required for in-app notifications")
        
        # print("TESSTTT")
        
        doc = {
            "user_id": payload.user_id,
            "type": payload.type,
            "message": payload.message,
            "timestamp": datetime.utcnow(),
        }
        notification.insert_one(doc)
        return {"message": "Notification created successfully",
                "notification": format_notification(doc)}
        
    elif payload.type == "email":
        if not payload.email:
            raise HTTPException(status_code=400, detail="email is required for email notifications")
        send_email(payload.email, payload.message)
        return {"message": f"Email notification sent successfully to ${payload.email}"}
    
    elif payload.type == "sms":
        if not payload.phone_number:
            raise HTTPException(status_code=400, detail="phone_number is required for SMS notifications")
        send_sms(payload.phone_number, payload.message)
        return {"message": f"SMS notification sent successfully to ${payload.phone_number}"}
        
@router.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: str):
    user_notifications = notification.find({"user_id": user_id})
    return [format_notification(notification) for notification in user_notifications]