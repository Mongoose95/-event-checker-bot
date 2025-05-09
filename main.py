import requests
import os

# Legge le variabili ambiente da Render
TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID")

# Funzione che invia un messaggio Telegram
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_USER_ID, "text": text}
    try:
        response = requests.post(url, data=payload)
        print("Notifica Telegram inviata:", response.text)
    except Exception as e:
        print("Errore nell'invio della notifica Telegram:", e)

# Funzione principale del bot
def start_bot():
    send_telegram_message("✅ Test Telegram: la notifica funziona!")
    return True

# Avvia lo script
if __name__ == "__main__":
    start_bot()
