from selenium.webdriver.common.by import By

class CheckoutStepOne:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, fname, lname, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(fname)
        self.driver.find_element(*self.LAST_NAME).send_keys(lname)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()