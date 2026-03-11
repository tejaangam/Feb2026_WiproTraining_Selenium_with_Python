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
class Test_links:

    def test_link(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/download")
        driver.maximize_window()
        time.sleep(2)

        links = driver.find_element(By.TAG_NAME, "a")
        count=len(links)
        print(count)

        for link in links:
            print(link.text)

        time.sleep(2)
        driver.close()
