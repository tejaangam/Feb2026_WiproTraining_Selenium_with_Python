from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class ManagerPage:

    def __init__(self, driver):
        self.driver = driver

    add_customer_btn = (By.XPATH, "//button[normalize-space()='Add Customer']")
    first_name = (By.XPATH, "//input[@placeholder='First Name']")
    last_name = (By.XPATH, "//input[@placeholder='Last Name']")
    post_code = (By.XPATH, "//input[@placeholder='Post Code']")
    submit_btn = (By.XPATH, "//button[@type='submit']")

    open_account_btn = (By.XPATH, "//button[normalize-space()='Open Account']")
    customer_dropdown = (By.ID, "userSelect")
    currency_dropdown = (By.ID, "currency")

    def add_customer(self, fname, lname, pcode):
        self.driver.find_element(*self.add_customer_btn).click()
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.post_code).send_keys(pcode)
        self.driver.find_element(*self.submit_btn).click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()

    def open_account(self, customer_index, currency_index):
        self.driver.find_element(*self.open_account_btn).click()

        Select(self.driver.find_element(*self.customer_dropdown)).select_by_index(customer_index)
        Select(self.driver.find_element(*self.currency_dropdown)).select_by_index(currency_index)

        self.driver.find_element(*self.submit_btn).click()

        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.accept()