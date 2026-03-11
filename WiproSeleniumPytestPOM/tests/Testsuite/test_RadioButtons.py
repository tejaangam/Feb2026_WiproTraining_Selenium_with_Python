import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_radio:
    def test_radio(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://rahulshettyacademy.com/AutomationPractice/')




        time.sleep(4)
        # click on login button

        Radio = driver.find_element(By.XPATH, "//input[@value='radio1']")
        Radio.click()

        assert "Practice Page" in driver.title
        driver.quit()





