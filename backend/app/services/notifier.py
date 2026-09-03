import os
from dotenv import load_dotenv
try:
    from twilio.rest import Client
except Exception:
    Client = None

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")

def send_sms(to_number: str, body: str):
    if not (TWILIO_SID and TWILIO_TOKEN and TWILIO_FROM and Client):
        print("[notifier] Twilio not configured or client not installed; skipping SMS. Message would be:", body)
        return False
    client = Client(TWILIO_SID, TWILIO_TOKEN)
    msg = client.messages.create(body=body, from_=TWILIO_FROM, to=to_number)
    return msg.sid
