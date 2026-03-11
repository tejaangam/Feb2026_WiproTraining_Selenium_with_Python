# pages/login_page.py

from selenium.webdriver.common.by import By
from ..base.base_page import BasePage

class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        try:
            self.send_keys(self.USERNAME_INPUT, username)
            self.send_keys(self.PASSWORD_INPUT, password)
            self.click(self.LOGIN_BUTTON)
        except Exception as e:
            print("Login failed:", e)