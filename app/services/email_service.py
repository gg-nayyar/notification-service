import os
import smtplib
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv(verbose=True, override=True)

EMAIL_USER = os.getenv("EMAIL_USER", "").strip()
EMAIL_PASS = os.getenv("EMAIL_PASS", "").strip()

def send_email(to_email:str, body:str):
    msg = EmailMessage()
    msg.set_content(body)
    msg["Subject"] = "Notification"
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    
    with smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT"))) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)