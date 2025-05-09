import requests
import os

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID")

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_USER_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        print("Notifica Telegram inviata:", response.text)
    except Exception as e:
        print("Errore nell'invio della notifica Telegram:", e)

def start_bot():
    send_telegram_message("✅ Test Telegram: la notifica funziona!")
    return True

if __name__ == "__main__":
    start_bot()
