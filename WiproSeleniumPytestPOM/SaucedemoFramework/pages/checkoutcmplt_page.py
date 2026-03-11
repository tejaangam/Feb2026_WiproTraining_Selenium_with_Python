from selenium.webdriver.common.by import By

class CheckoutComplete:

    SUCCESS_MSG = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MSG).text