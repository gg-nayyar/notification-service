import os
from celery import Celery
from dotenv import load_dotenv
from app.services.sms_service import send_sms
from app.services.email_service import send_email

load_dotenv()

celery = Celery("tasks", broker=os.getenv("CELERY_BROKER_URL"))

@celery.task
def send_email_task(email:str, message:str):
    print("[DEBUG] Sending email task")
    send_email(email, message)
    
@celery.task
def send_sms_task(phone:str, message:str):
    print("[DEBUG] Sending SMS task")
    send_sms(phone, message)