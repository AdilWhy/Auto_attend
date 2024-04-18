import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import RemoteVersion
from configurations import settings
import requests

driver = RemoteVersion.remoteDriver

def loginTo():
    id_login = (WebDriverWait(driver, 3).until(EC.element_to_be_clickable((By.ID, "gwt-uid-4"))))
    id_login.clear()
    id_login.send_keys(settings.login)
    time.sleep(5)
    WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'gwt-uid-6'))).send_keys(settings.password, Keys.ENTER)
    attend()

def check_logout():
    time.sleep(5)
    try:
        text = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='v-label v-widget v-label-undef-w']"))).text
        if text == 'Вход в систему':
            driver.quit()
            time.sleep(5)
    except:
        driver.refresh()



def attend():
    while True:
        check_logout()
        try:
            wait = WebDriverWait(driver, 30)
            element = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='v-button v-widget primary v-button-primary']")))
            element.click()
            text = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='v-label v-widget bold v-label-bold v-has-width']"))).text
            lesson = text.split('\n')[0]
            msg = "Attended" + '\n' + lesson
            send_message(msg, settings.CHAT_ID)
        except:
            driver.refresh()
            

def send_message(msg, CHAT_ID):
    url = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}"
    print(requests.get(url).json())


def main():
    url = "https://wsp.kbtu.kz/RegistrationOnline"
    driver.get(url)
    loginTo()


if __name__ == "__main__":
    main()
