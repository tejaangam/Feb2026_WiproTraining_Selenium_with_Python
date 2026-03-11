from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class CustomerPage:

    def __init__(self, driver):
        self.driver = driver

    user_dropdown = (By.ID, "userSelect")
    login_btn = (By.XPATH, "//button[@type='submit']")
    deposit_btn = (By.XPATH, "//button[normalize-space()='Deposit']")
    withdraw_btn = (By.XPATH, "//button[normalize-space()='Withdrawl']")
    amount_input = (By.XPATH, "//input[@placeholder='amount']")
    submit_btn = (By.XPATH, "//button[@type='submit']")
    transactions_btn = (By.XPATH, "//button[normalize-space()='Transactions']")

    def login_customer(self, index):
        Select(self.driver.find_element(*self.user_dropdown)).select_by_index(index)
        self.driver.find_element(*self.login_btn).click()

    def deposit(self, amount):
        self.driver.find_element(*self.deposit_btn).click()
        self.driver.find_element(*self.amount_input).send_keys(amount)
        self.driver.find_element(*self.submit_btn).click()

    def withdraw(self, amount):
        self.driver.find_element(*self.withdraw_btn).click()
        self.driver.find_element(*self.amount_input).send_keys(amount)
        self.driver.find_element(*self.submit_btn).click()

    def view_transactions(self):
        self.driver.find_element(*self.transactions_btn).click()