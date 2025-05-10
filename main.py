from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
import requests
import os
import sys

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
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)

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
                send_telegram_message("position WAM open now\nApri il sito qui:\nhttps://emexprod-c6t5hv8lbf.dispatcher.hana.ondemand.com/index.html#/ya1xemg0869ah4cel1wm")
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
    if len(sys.argv) > 1:
        if sys.argv[1] == "daily_check":
            send_telegram_message("✅ Il programma è attivo e funzionante.")
        elif sys.argv[1] == "check_manual":
            send_telegram_message("✅ Sistema funzionante. Job attivo.")
    else:
        start_bot()
