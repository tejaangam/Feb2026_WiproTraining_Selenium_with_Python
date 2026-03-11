import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager


class Test_Alerts:
    def test_alerts(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        time.sleep(4)
        simplealt = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']" )
        simplealt.click()
        alt = driver.switch_to.alert
        alt.accept()
        time.sleep(3)

        #confirm alert
        confalt  = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Confirm']")
        confalt.click()
        alt = driver.switch_to.alert
        alt.dismiss()
        time.sleep(3)
        #prompt alert
        promptalt = driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Prompt']")
        promptalt.click()
        alt = driver.switch_to.alert
        alerttext = alt.text
        print(alerttext)
        alt.send_keys("test hello")
        time.sleep(2)
        alt.accept()
        time.sleep(3)

        driver.quit()





