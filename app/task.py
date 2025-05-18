import os
from celery import Celery, Task
from dotenv import load_dotenv
from app.services.sms_service import send_sms
from app.services.email_service import send_email

load_dotenv()

celery = Celery("tasks", broker=os.getenv("CELERY_BROKER_URL"))

class RetryTask(Task):
    autoretry_for = (Exception,)
    retry_kwargs = {"max_retries": 5, "countdown": 7}
    retry_backoff = True
    retry_jitter = True

@celery.task(base=RetryTask)
def send_email_task(email:str, message:str):
    print("[DEBUG] Sending email task")
    send_email(email, message)
    
@celery.task(base=RetryTask)
def send_sms_task(phone:str, message:str):
    print("[DEBUG] Sending SMS task")
    send_sms(phone, message)