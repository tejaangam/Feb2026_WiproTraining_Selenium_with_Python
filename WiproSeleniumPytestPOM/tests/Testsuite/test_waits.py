import pytest
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class waits:
    def test_fails(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
        driver.find_element(By.ID, "adder").click()

        with pytest.raises(NoSuchElementException):
            driver.find_element(By.ID, 'box0')


        def test_sleep(driver):
            driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
            driver.find_element(By.ID, "adder").click()

        time.sleep(2)
        added = driver.find_element(By.ID, "box0")

        assert added.get_dom_attribute('class') == "redbox"


        def test_implicit(driver):
            driver.implicitly_wait(2)
            driver.get('https://www.selenium.dev/selenium/web/dynamic.html')
            driver.find_element(By.ID, "adder").click()

            added = driver.find_element(By.ID, "box0")

            assert added.get_dom_attribute('class') == "redbox"


