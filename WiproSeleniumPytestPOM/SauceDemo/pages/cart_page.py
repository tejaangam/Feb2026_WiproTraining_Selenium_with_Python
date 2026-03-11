# pages/cart_page.py

from selenium.webdriver.common.by import By
from ..base.base_page import BasePage

class CartPage(BasePage):

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def click_checkout(self):
        try:
            self.click(self.CHECKOUT_BUTTON)
        except Exception as e:
            print("Checkout click failed:", e)