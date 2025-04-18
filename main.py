import requests
import time
import os

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
TEXT = "📢 هذا اختبار تلقائي من FastNews 🔥"

def send_message():
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": TEXT
    }
    try:
        response = requests.post(url, data=payload)
        print(response.status_code, response.json())
    except Exception as e:
        print("Error sending message:", e)

# إرسال كل ساعتين تقريبًا
while True:
    send_message()
    time.sleep(7200)
