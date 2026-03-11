from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    bank_manager_login = (By.XPATH, "//button[normalize-space()='Bank Manager Login']")
    customer_login = (By.XPATH, "//button[normalize-space()='Customer Login']")

    def click_bank_manager_login(self):
        self.driver.find_element(*self.bank_manager_login).click()

    def click_customer_login(self):
        self.driver.find_element(*self.customer_login).click()