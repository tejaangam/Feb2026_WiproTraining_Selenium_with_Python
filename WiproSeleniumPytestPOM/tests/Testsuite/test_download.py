import os
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager

DOWNLOAD_DIR ="C://Users//hp//Downloads"
class Test_download:

    def test_dd(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        alert = driver.find_element(By.XPATH, "//a[normalize-space()='alert.jpeg']")
        alert.click()

        #verify file download
        file_path = os.path.join(DOWNLOAD_DIR, "alert.jpeg")
        assert os.path.exists(file_path)

        time.sleep(3)
        driver.close()
