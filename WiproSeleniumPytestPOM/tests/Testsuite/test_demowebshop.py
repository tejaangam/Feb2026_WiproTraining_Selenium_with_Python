# test_demowebshop.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

from webdriver_manager.firefox import GeckoDriverManager


def test_demowebshop_end_to_end():

    # ---------- Browser Setup ----------
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
      options=chrome_options)



    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://demowebshop.tricentis.com/")
        time.sleep(2)

        # ---------- Click Register ----------
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)

        # ---------- Register New User ----------
        random_number = random.randint(1000, 9999)
        email = f"testuser{random_number}@mail.com"
        password = "Test@123"

        gender = (driver.find_element(By.ID, "gender-male"))
        driver.click()
        firstname = (driver.find_element(By.ID, "FirstName"))
        driver.send_keys("Teju")
        driver.find_element(By.ID, "LastName").send_keys("Angam")
        driver.find_element(By.ID, "Email").send_keys(email)
        driver.find_element(By.ID, "Password").send_keys(password)
        driver.find_element(By.ID, "ConfirmPassword").send_keys(password)
        driver.find_element(By.ID, "register-button").click()
        print("Registration Successful")

        # ---------- Continue ----------
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "register-continue-button"))).click()
        time.sleep(2)

        # ---------- Add Product To Cart ----------
        driver.find_element(By.XPATH, "//div[2]//div[1]//div[2]//div[3]//div[2]//input[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientName']").send_keys("Teja")
        driver.find_element(By.XPATH, "//input[@id='giftcard_2_RecipientEmail']").send_keys(email)
        driver.find_element(By.XPATH, " // input[ @ id = 'add-to-cart-button-2']")
        # ---------- Go To Cart ----------
        driver.find_element(By.LINK_TEXT, "Shopping cart").click()
        time.sleep(2)

        # ---------- Accept Terms ----------
        driver.find_element(By.ID, "termsofservice").click()

        driver.find_element(By.ID, "checkout").click()
        time.sleep(3)

        # ---------- Billing Address ----------
        Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_visible_text("India")

        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Hyderabad")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Main Street")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("500001")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("9999999999")

        driver.find_element(By.XPATH, "//input[@onclick='Billing.save()']").click()
        time.sleep(2)

        # ---------- Shipping Method ----------
        driver.find_element(By.XPATH, "//input[@onclick='ShippingMethod.save()']").click()
        time.sleep(2)

        # ---------- Payment Method ----------
        driver.find_element(By.XPATH, "//input[@onclick='PaymentMethod.save()']").click()
        time.sleep(2)

        # ---------- Payment Info ----------
        driver.find_element(By.XPATH, "//input[@onclick='PaymentInfo.save()']").click()
        time.sleep(2)

        # ---------- Confirm Order ----------
        driver.find_element(By.XPATH, "//input[@onclick='ConfirmOrder.save()']").click()

        # ---------- Verify Order ----------
        success_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        ).text

        print("Order Status:", success_message)

        assert "successfully processed" in success_message

        print("Order Completed Successfully ✅")

    except Exception as e:
        print("Test Failed ❌", e)

    finally:
        time.sleep(3)
        driver.quit()