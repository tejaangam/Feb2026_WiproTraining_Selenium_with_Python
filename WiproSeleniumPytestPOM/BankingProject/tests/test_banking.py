import time
from BankingProject.pages.login_page import LoginPage
from BankingProject.pages.manager_page import ManagerPage
from BankingProject.pages.customer_page import CustomerPage

def test_end_to_end_bank_flow(driver):

    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    login = LoginPage(driver)
    manager = ManagerPage(driver)
    customer = CustomerPage(driver)

    login.click_bank_manager_login()
    time.sleep(2)

    manager.add_customer("rohit", "sharma", "508111")
    time.sleep(2)

    manager.open_account(2, 3)
    time.sleep(2)

    driver.find_element("xpath", "//button[@class='btn home']").click()
    login.click_customer_login()
    time.sleep(2)

    customer.login_customer(3)
    time.sleep(2)

    customer.deposit(200)
    time.sleep(2)

    customer.withdraw(200)
    time.sleep(2)

    customer.view_transactions()
    time.sleep(3)

    assert "Transaction" in driver.page_source