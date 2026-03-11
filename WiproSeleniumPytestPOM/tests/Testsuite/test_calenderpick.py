from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
class cale:
    def calender(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://rsuitejs.com/components/date-picker/")
        driver.maximize_window()
        time.sleep(2)

        cal=driver.find_element(By.XPATH,"(//*[name()='svg'][@aria-label='calender simple'])[1]")
        cal.click()
        time.sleep(3)
        date=driver.find_element(By.XPATH,"(//span[normalize-space()='24'])[1]")
        date.click()
        time.sleep(3)
        click_ok=driver.find_element(By.XPATH,"//button[normalize-space()='OK']")
        click_ok.click()
        time.sleep(5)
        driver.close()