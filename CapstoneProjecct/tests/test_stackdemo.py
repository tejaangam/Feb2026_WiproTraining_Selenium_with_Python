import os
import time
import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utilities.excel_reader import ExcelReader
from utilities.logger import get_logger

logger = get_logger()

excel = ExcelReader()
data = excel.get_data(
    "C:/Users/hp/PycharmProjects/CapstoneProjecct/data/test_data.xlsx",
    "Sheet1"
)

def login_and_search(driver):

    login = LoginPage(driver)
    product = ProductPage(driver)

    row = data.iloc[0]
    driver.get("https://bstackdemo.com/")
    logger.info("Login started")
    login.login(row["username"],row["password"])
    logger.info("Searching product")
    product.search_product(row["product"])
    return row

#LOGIN TEST
def test_login(setup):

    driver = setup
    login = LoginPage(driver)

    try:
        for index, row in data.iterrows():
            driver.get("https://bstackdemo.com/")
            username = row["username"]
            time.sleep(2)
            password = row["password"]
            logger.info("Login started")
            login.login(username, password)
        logger.info("Login Test Passed")
        assert "StackDemo" in driver.title
    except Exception as e:
        logger.error("Login test failed: " + str(e))
        pytest.fail(str(e))


#  PRODUCT SEARCH
def test_product_search(setup):

    driver = setup
    login = LoginPage(driver)
    product = ProductPage(driver)

    try:
        row = login_and_search(driver)
        logger.info("Product search successful")
    except Exception as e:
        logger.error("Product search failed: " + str(e))
        pytest.fail(str(e))

#  ADD TO CART
def test_add_to_cart(setup):

    driver = setup
    login = LoginPage(driver)
    product = ProductPage(driver)
    try:
        row = login_and_search(driver)
        logger.info("Adding product to cart")
        product.add_product()
        logger.info("Product added to cart successful")
    except Exception as e:
        logger.error("Adding product to cart failed: " + str(e))
        pytest.fail(str(e))

#  CHECKOUT
def test_checkout(setup):

    driver = setup
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    try:
        row = login_and_search(driver)
        product.add_product()
        logger.info("Checkout started")
        cart.checkout_process()
        logger.info("Checkout completed")
    except Exception as e:
        logger.error("Checkout Failed: " + str(e))
        pytest.fail(str(e))

#  SHIPPING DETAILS
def test_shipping_details(setup):

    driver = setup
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    try:
        row = login_and_search(driver)
        product.add_product()
        cart.checkout_process()
        logger.info("Entering shipping details")
        checkout.enter_shipping_details(
            row["firstname"],
            row["lastname"],
            row["address"],
            row["city"],
            row["state"],
            row["zipcode"]
        )
        logger.info("Shipping details entered")
    except Exception as e:
        logger.error("Entering shipping details failed: " + str(e))
        pytest.fail(str(e))

#  DOWNLOAD RECEIPT
def test_download_receipt(setup):

    driver = setup
    login = LoginPage(driver)
    product = ProductPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    try:
        row = login_and_search(driver)
        product.add_product()
        cart.checkout_process()
        checkout.enter_shipping_details(
            row["firstname"],
            row["lastname"],
            row["address"],
            row["city"],
            row["state"],
            row["zipcode"]
        )
        logger.info("Downloading receipt")
        checkout.download_receipt()
        logger.info("Validating receipt")
        download_path = "C://Users//hp//Downloads"
        time.sleep(5)
        files = os.listdir(download_path)
        receipt_found = False
        for file in files:
            if "confirmation" in file.lower():
                receipt_found = True
                break
        assert receipt_found, "Receipt file not downloaded"
        logger.info("Receipt validation successful")
    except Exception as e:
        logger.error("Download receipt failed: " + str(e) )
        pytest.fail(str(e))