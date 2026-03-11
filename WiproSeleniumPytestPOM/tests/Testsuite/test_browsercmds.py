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

        driver.get("https://trytestingthis.netlify.app/")
        driver.maximize_window()
        time.sleep(2)

        #browser interactions
        title = driver.title
        print(title)
        url = driver.current_url
        print(url)

        #navigational commands
        driver.back()
        time.sleep(2)

        driver.forward()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

        driver.close()
