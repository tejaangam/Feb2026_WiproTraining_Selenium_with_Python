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

        driver.get("https://the-internet.herokuapp.com/windows")
        driver.maximize_window()
        time.sleep(2)

        clickhere = driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']")
        clickhere.click()

        #fetch the window handles of both tabs
        windows = driver.window_handles
        print(windows)

        #move control to the child window
        driver.switch_to.window(windows[1])
        text = driver.find_element(By.TAG_NAME, "h3")
        print(text)
        driver.close()

        #get back to parent window
        driver.switch_to.window(windows[0])
        clickhere.is_displayed()

        driver.close()