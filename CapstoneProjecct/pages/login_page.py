from selenium.webdriver.common.by import By
from pages.basepage import BasePage
#from utilities.logger import get_logger

#logger = get_logger()

class LoginPage(BasePage):

    signin_btn = (By.ID, "signin")
    username_dropdown = (By.ID, "username")
    password_dropdown = (By.ID, "password")
    login_btn = (By.ID, "login-btn")

    def login(self, username, password):

        try:
            #logger.info("Clicking Sign In button")
            self.click(self.signin_btn)

            #logger.info("Opening username dropdown")
            self.click(self.username_dropdown)

            #logger.info("Selecting username")
            self.click((By.XPATH, f"//div[text()='{username}']"))

            #logger.info("Opening password dropdown")
            self.click(self.password_dropdown)

            #logger.info("Selecting password")
            self.click((By.XPATH, f"//div[text()='{password}']"))

            #logger.info("Clicking login button")
            self.click(self.login_btn)

        except Exception as e:
            #logger.error("Login failed: " + str(e))
            raise