import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv(verbose=True, override=True)

def send_sms(to_number: str, message: str):
    client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    client.messages.create(
        body=message,
        from_=os.getenv("TWILIO_PHONE"),
        to=to_number
    )