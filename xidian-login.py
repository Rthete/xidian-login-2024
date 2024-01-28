from datetime import datetime
import logging
import requests
import sys
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service as ChromeService
import time

current_time = datetime.now().strftime("%Y%m%d%H%M%S")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


login_ip = "https://w.xidian.edu.cn/srun_portal_pc?ac_id=1&theme=pro"
username = ""
password = ""
driver_path = ""

def test_connection():
    try:
        response = requests.get("https://www.baidu.com/", timeout=5)
        if(response.status_code == 200):
            logging.info("testing over, already connected to internet, exit")
            sys.exit()
    except Exception as e:
        logging.warning(e)


def login():
    options = Options()
    options.add_argument('headless')
    service = ChromeService(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    try:
        driver.get(login_ip)
    except Exception as e:
        logging.error(f"failed to get: {e}")
        logging.error("please check ethernet")
        return

    driver.implicitly_wait(3)

    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-account").send_keys(Keys.ENTER)

    time.sleep(1)
    driver.quit()
    test_connection()


if __name__ == '__main__':
    logging.info("testing connection...")
    test_connection()
    while True:
        logging.info("try logging in...")
        login()
        time.sleep(120)
