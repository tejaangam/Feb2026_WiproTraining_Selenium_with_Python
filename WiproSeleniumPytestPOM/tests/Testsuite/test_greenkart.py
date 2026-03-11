# test_greenkart.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_greenkart_end_to_end():

    # ---------- Browser Setup ----------
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")


    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    wait = WebDriverWait(driver, 10)

    try:
        # ---------- Open Website ----------
        driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
        time.sleep(2)

        # ---------- Add Products To Cart ----------
        products = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")

        # Add first 3 products
        for i in range(3):
            products[i].click()
            time.sleep(1)

        # ---------- Click Cart Icon ----------
        driver.find_element(By.CLASS_NAME, "cart-icon").click()
        time.sleep(4)

        # ---------- Proceed To Checkout ----------
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='PROCEED TO CHECKOUT']"))).click()
        time.sleep(4)

        # ---------- Place Order ----------
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))).click()
        time.sleep(4)

        # ---------- Select Country (India) ----------
        country_dropdown = Select(wait.until(
            EC.visibility_of_element_located((By.TAG_NAME, "select"))
        ))

        country_dropdown.select_by_visible_text("India")
        time.sleep(4)

        # ---------- Agree Terms ----------
        driver.find_element(By.CLASS_NAME, "chkAgree").click()
        time.sleep(4)

        # ---------- Click Proceed ----------
        driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
        time.sleep(4)

        # ---------- Validate Success Message ----------
        success_message = wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "wrapperTwo"))
        ).text

        print("Order Message:", success_message)

        assert "Thank you" in success_message

        print("Test Passed Successfully")

    except Exception as e:
        print("Test Failed:", e)

    finally:
        time.sleep(4)
        driver.quit()