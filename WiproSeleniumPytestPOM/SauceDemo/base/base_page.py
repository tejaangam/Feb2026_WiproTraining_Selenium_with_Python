# base/base_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Generic method to click element
    def click(self, by_locator):
        try:
            element = self.wait.until(EC.element_to_be_clickable(by_locator))
            element.click()
        except Exception as e:
            print("Error while clicking element:", e)

    # Generic method to send keys
    def send_keys(self, by_locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print("Error while entering text:", e)

    # Get text of element
    def get_text(self, by_locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(by_locator))
            return element.text
        except Exception as e:
            print("Error while getting text:", e)
            return None