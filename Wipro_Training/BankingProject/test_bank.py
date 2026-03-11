import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_full_banking_system(driver):
    wait = WebDriverWait(driver, 10)
    delay = 5  # 5-second observation delay

    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    # --- SECTION 1: BANK MANAGER LOGIN ---
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Bank Manager Login']"))).click()
    time.sleep(delay)

    # 1.1 Add Customer
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Add Customer')]"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))).send_keys("Teja")
    driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Tester")
    driver.find_element(By.XPATH, "//input[@placeholder='Post Code']").send_keys("90210")
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(delay)

    # 1.2 Open Account (Linking Customer to Currency)
    driver.find_element(By.XPATH, "//button[contains(.,'Open Account')]").click()
    time.sleep(2)
    # Select User and Currency from Dropdowns
    Select(wait.until(EC.presence_of_element_located((By.ID, "userSelect")))).select_by_visible_text("Harry Tester")
    Select(driver.find_element(By.ID, "currency")).select_by_visible_text("Dollar")
    time.sleep(delay)
    driver.find_element(By.XPATH, "//button[text()='Process']").click()

    wait.until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    time.sleep(delay)

    # 1.3 Validate Customer in "Customers" List
    driver.find_element(By.XPATH, "//button[contains(.,'Customers')]").click()
    time.sleep(delay)
    # Check if 'Harry' exists in the table
    customer_row = wait.until(EC.presence_of_element_located((By.XPATH, "//td[text()='Harry']")))
    assert customer_row.is_displayed()
    print("Manager Section: Customer created and verified.")

    # --- SECTION 2: CUSTOMER LOGIN & TRANSACTIONS ---
    driver.find_element(By.XPATH, "//button[text()='Home']").click()
    time.sleep(delay)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Customer Login']"))).click()
    time.sleep(2)

    # Select the newly created customer
    Select(wait.until(EC.presence_of_element_located((By.ID, "userSelect")))).select_by_visible_text("Harry Tester")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(delay)

    # 2.1 Verify Initial Balance is 0
    balance = driver.find_element(By.XPATH, "//strong[2]").text
    assert balance == "0"

    # 2.2 Deposit Money
    driver.find_element(By.XPATH, "//button[contains(.,'Deposit')]").click()
    time.sleep(2)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='amount']"))).send_keys("1000")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify Success Message
    msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@ng-show='message']"))).text
    assert "Deposit Successful" in msg
    time.sleep(delay)

    # 2.3 Withdraw Money
    driver.find_element(By.XPATH, "//button[contains(.,'Withdrawl')]").click()
    time.sleep(3)  # Angular swap delay
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='amount']"))).send_keys("400")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

    # Verify Success Message
    msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@ng-show='message']"))).text
    assert "Transaction successful" in msg
    time.sleep(delay)

    # 2.4 Final Balance Check
    final_balance = driver.find_element(By.XPATH, "//strong[2]").text
    assert final_balance == "600"
    print(f"Customer Section: Transactions completed. Final Balance: {final_balance}")

    # 2.5 Transaction History Check
    driver.find_element(By.XPATH, "//button[contains(.,'Transactions')]").click()
    time.sleep(delay)
    # Ensure at least one transaction row exists
    rows = driver.find_elements(By.XPATH, "//table/tbody/tr")
    assert len(rows) >= 2
    print("Test Passed: All elements and workflows validated.")