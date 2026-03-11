import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_dd:
    def test_dd(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://the-internet.herokuapp.com/upload")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        browse = driver.find_element(By.XPATH, "//input[@id='file-upload']")
        browse.send_keys("C:/Users/hp/Downloads/sample.jpg")
        time.sleep(2)
        fileupload = driver.find_element(By.XPATH, "//h3[normalize-space()='File-Uploaded!']")
        assert fileupload.text == "File Uploaded"
        time.sleep(3)
        driver.close()
