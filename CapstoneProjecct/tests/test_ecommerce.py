import os
import time
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utilities import logger
from utilities.excel_reader import ExcelReader
from utilities.logger import get_logger

logger = get_logger()
logger.info("Starting Test Flow")

def test_ecommerce_flow(setup):

    driver = setup

    excel = ExcelReader()

    data = excel.get_data(
        "C:/Users/hp/PycharmProjects/CapstoneProjecct/data/test_data.xlsx",
        "Sheet1"
    )

    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    for index, row in data.iterrows():

        try:

            driver.get("https://bstackdemo.com/")

            username = row["username"]
            password = row["password"]
            product_name = row["product"]

            firstname = row["firstname"]
            lastname = row["lastname"]
            address = row["address"]
            city = row["city"]
            state = row["state"]
            zipcode = row["zipcode"]

            #Sign In
            logger.info("Login started")
            login.login(username, password)

            #Product Search
            logger.info("Searching product")
            product.search_product(product_name)


            #Adding to cart
            logger.info("Adding to cart")
            product.add_product()

            #Checkout
            logger.info("Checkout started")
            cart.checkout_process()

            #Shipping details
            logger.info("Entering shipping details")
            checkout.enter_shipping_details(firstname, lastname, address, city, state, zipcode)

            #Receipt Downloading
            logger.info("Downloading receipt")
            checkout.download_receipt()

            #Validating Receipt
            logger.info("Validating Receipt")
            download_path = "C://Users//hp//Downloads"
            time.sleep(5)
            files = os.listdir(download_path)
            receipt_found = False
            for file in files:
                if "confirmation" in file.lower():
                    receipt_found = True
                    break
            assert receipt_found, "Receipt file not downloaded"

        except Exception as e:
            logger.error("Test Failed")
            pytest.fail(str(e))