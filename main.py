from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import requests
import os

# Variabili di ambiente per Telegram
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
    def start_bot():
    send_telegram_message("✅ Test Telegram: la notifica funziona!")
    return True


    try:
        driver.get("https://emexprod-c6t5hv8lbf.dispatcher.hana.ondemand.com/index.html#/ya1xemg0869ah4cel1wm")
        time.sleep(5)

        driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]').click()
        time.sleep(5)

        today = datetime.today().strftime("%d/%m/%Y")
        start_date_input = driver.find_element(By.XPATH, '//input[contains(@placeholder, "Enter start date")]')
        start_date_input.clear()
        start_date_input.send_keys(today)
        time.sleep(2)

        driver.find_element(By.XPATH, '//button[contains(text(), "Continue")]').click()
        time.sleep(10)

        try:
            selectable = driver.find_element(By.XPATH, '//input[@type="radio" or @type="checkbox"]')
            if selectable:
                send_telegram_message("🚨 Evento disponibile! Vai subito al sito per selezionare l'opzione.")
                print("Evento trovato! Notifica Telegram inviata.")
                return True
        except NoSuchElementException:
            print("Nessun evento trovato. Ritenterò.")

    except Exception as e:
        print(f"Errore: {e}")
    finally:
        driver.quit()

    return False

if __name__ == "__main__":
    start_bot()
