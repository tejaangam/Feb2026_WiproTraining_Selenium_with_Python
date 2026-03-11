import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
class Test_WH:

    def test_wh(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://jqueryui.com/datepicker/")
        driver.maximize_window()
        time.sleep(2)

        #frame = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(0)

        time.sleep(2)

        datepicker = driver.find_element(By.XPATH, "//input[@id='datepicker']")
        datepicker.click()
        clickdate = driver.find_element(By.XPATH, "//a[normalize-space()='25']")
        clickdate.click()
        time.sleep(2)
        driver.close()