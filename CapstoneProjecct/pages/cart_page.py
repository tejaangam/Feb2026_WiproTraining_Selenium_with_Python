from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utilities.logger import get_logger

logger = get_logger()


class CartPage(BasePage):
    checkout_btn = (By.XPATH, "//div[@class='buy-btn']")
    def checkout_process(self):
        try:
            #logger.info("Clicking checkout button")
            self.click(self.checkout_btn)
        except Exception as e:
            #logger.error("Checkout failed: " + str(e))
            raise