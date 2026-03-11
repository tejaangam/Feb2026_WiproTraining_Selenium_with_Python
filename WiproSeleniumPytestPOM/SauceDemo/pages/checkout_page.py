# pages/checkout_page.py

from selenium.webdriver.common.by import By
from ..base.base_page import BasePage

class CheckoutPage(BasePage):

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    THANK_YOU_TEXT = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def fill_information(self, first, last, postal):
        try:
            self.send_keys(self.FIRST_NAME, first)
            self.send_keys(self.LAST_NAME, last)
            self.send_keys(self.POSTAL_CODE, postal)
            self.click(self.CONTINUE_BUTTON)
        except Exception as e:
            print("Filling information failed:", e)

    def finish_order(self):
        try:
            self.click(self.FINISH_BUTTON)
        except Exception as e:
            print("Finish order failed:", e)

    def get_confirmation_message(self):
        return self.get_text(self.THANK_YOU_TEXT)

    def back_to_home(self):
        try:
            self.click(self.BACK_HOME_BUTTON)
        except Exception as e:
            print("Back to home failed:", e)