# pages/inventory_page.py

from selenium.webdriver.common.by import By
from ..base.base_page import BasePage

class InventoryPage(BasePage):

    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart(self):
        try:
            self.click(self.ADD_TO_CART_BUTTON)
        except Exception as e:
            print("Add to cart failed:", e)

    def go_to_cart(self):
        try:
            self.click(self.CART_ICON)
        except Exception as e:
            print("Cart navigation failed:", e)