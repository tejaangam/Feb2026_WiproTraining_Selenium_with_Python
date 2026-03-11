# tests/test_e2e.py
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from SauceDemo.base.driver_factory import DriverFactory
from SauceDemo.config import BASE_URL, USERNAME, PASSWORD
from SauceDemo.pages.login_page import LoginPage
from SauceDemo.pages.inventory_page import InventoryPage
from SauceDemo.pages.cart_page import CartPage
from SauceDemo.pages.checkout_page import CheckoutPage

def test_Saucedemo():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver = DriverFactory.get_driver()

    driver.maximize_window()
    driver.get(BASE_URL)

    try:
        # Step 1: Login
        login_page = LoginPage(driver)
        login_page.login(USERNAME, PASSWORD)
        time.sleep(4)
        try:
            ok_button = driver.find_element(By.XPATH, "//button[text()='OK]")
            ok_button.click()
            print("password popup handled")
        except:
            print("No password popup found")
        time.sleep(3)
        # Step 2: Add to Cart
        inventory_page = InventoryPage(driver)
        inventory_page.add_product_to_cart()
        time.sleep(4)
        # Step 3: Go to Cart
        inventory_page.go_to_cart()
        time.sleep(4)
        # Step 4: Checkout
        cart_page = CartPage(driver)
        cart_page.click_checkout()
        time.sleep(4)
        # Step 5: Fill Information
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_information("Teju", "Angam", "500001")
        time.sleep(4)
        # Step 6: Finish Payment
        checkout_page.finish_order()
        time.sleep(4)
        # Step 7: Verify Thank You Message
        message = checkout_page.get_confirmation_message()
        print("Order Message:", message)
        time.sleep(4)
        assert "Thank you for your order!" in message
        # Step 8: Back to Home
        checkout_page.back_to_home()
    except Exception as e:
        print("Test Failed:", e)

    finally:
        driver.quit()
        