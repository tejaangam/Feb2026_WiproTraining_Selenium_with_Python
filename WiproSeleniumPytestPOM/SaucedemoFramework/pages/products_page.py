from selenium.webdriver.common.by import By

class ProductsPage:

    ADD_TO_CART = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product(self):
        self.driver.find_elements(*self.ADD_TO_CART)[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()