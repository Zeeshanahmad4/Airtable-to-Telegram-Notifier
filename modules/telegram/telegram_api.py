# telegram_api.py

import requests

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

TELEGRAM_SEND_MESSAGE_ENDPOINT = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

def send_message_to_telegram(text):
    """
    Send a message to the Telegram channel.
    """
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(TELEGRAM_SEND_MESSAGE_ENDPOINT, data=payload)
    return response.json()
 
