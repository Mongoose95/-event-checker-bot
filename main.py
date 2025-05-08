from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
from datetime import datetime
from pushbullet import Pushbullet

import os

PB_API_KEY = os.environ.get("PB_API_KEY")
pb = Pushbullet(PB_API_KEY)

def send_push_notification(title, message):
    pb.push_note(title, message)

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
                send_push_notification("Evento Disponibile!", "Vai subito al sito per selezionare l'opzione.")
                print("Evento trovato! Notifica inviata.")
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
