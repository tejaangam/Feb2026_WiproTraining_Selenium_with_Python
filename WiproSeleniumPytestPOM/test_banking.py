import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
time.sleep(3)

bank_manager_login=driver.find_element(By.XPATH,"//button[normalize-space()='Bank Manager Login']")
bank_manager_login.click()
time.sleep(3)

add_customer=driver.find_element(By.XPATH,"//button[normalize-space()='Add Customer']")
add_customer.click()
time.sleep(3)

First_name=driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
First_name.send_keys("varun")
time.sleep(2)

last_name=driver.find_element(By.XPATH,"//input[@placeholder='Last Name']")
last_name.send_keys("varun")
time.sleep(2)

post_code=driver.find_element(By.XPATH,"//input[@placeholder='Post Code']")
post_code.send_keys("508111")
time.sleep(2)

add_customer_click=driver.find_element(By.XPATH,"//button[@type='submit']")
add_customer_click.click()
time.sleep(3)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()
time.sleep(3)

open_account=driver.find_element(By.XPATH,"//button[normalize-space()='Open Account']")
open_account.click()
time.sleep(2)

customer_name=driver.find_element(By.XPATH,"//select[@id='userSelect']")
dropdown = Select(customer_name)
dropdown.select_by_index(2)
time.sleep(2)

currency=driver.find_element(By.XPATH,"//select[@id='currency']")
dropdown = Select(currency)
dropdown.select_by_index(3)

process_click=driver.find_element(By.XPATH,"//button[@type='submit']")
process_click.click()
time.sleep(3)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert.accept()
time.sleep(3)

driver.quit()