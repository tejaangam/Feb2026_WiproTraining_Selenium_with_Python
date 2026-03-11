import time
from selenium.webdriver.common.by import By
from pages.basepage import BasePage
#from utilities.logger import get_logger
#logger = get_logger()
class ProductPage(BasePage):
    search_box = (By.XPATH, "//input[@placeholder='Search']")
    search_button = (By.XPATH, "//button[contains(text(),'Search')]")
    add_to_cart = (By.CSS_SELECTOR, ".shelf-item__buy-btn")
    cart_icon = (By.ID, "shopping-cart")

    try:
        def search_product(self, product_name):
            #logger.info("Searching product")
            self.type(self.search_box, product_name)
            self.click(self.search_button)
            time.sleep(2)
        def add_product(self):
            #logger.info("Adding product to cart")
            self.click(self.add_to_cart)
    except Exception as e:
        raise








'''
checkout_btn = (By.XPATH, "//div[@class='float-cart__footer']//button")
        def checkout(self):
            #logger.info("Proceeding to checkout")
            checkout = self.get_element(self.checkout_btn)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", checkout
            )
            self.driver.execute_script(
                "arguments[0].click();", checkout
            )
'''