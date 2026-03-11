import time
import pytest
from SaucedemoFramework.pages.login_page import LoginPage
from SaucedemoFramework.pages.products_page import ProductsPage
from SaucedemoFramework.pages.cart_page import CartPage
from SaucedemoFramework.pages.checkout1_page import CheckoutStepOne
from SaucedemoFramework.pages.checkout2_page import CheckoutStepTwo
from SaucedemoFramework.pages.checkoutcmplt_page import CheckoutComplete
from SaucedemoFramework.utils.excel_reader import get_login_data
from utilities import logger
from utilities.logger import get_logger

logger = get_logger()
login_data = get_login_data("C:/Users/hp/PycharmProjects/WiproSeleniumPytestPOM/SaucedemoFramework/testdata/login_data.xlsx")


class TestSauceDemo:

    def test_complete_order_flow(self, setup):

        driver = setup

        login = LoginPage(driver)
        login.login("standard_user", "secret_sauce")

        products = ProductsPage(driver)
        products.add_first_product()
        products.go_to_cart()

        cart = CartPage(driver)
        cart.click_checkout()

        checkout1 = CheckoutStepOne(driver)
        checkout1.enter_details("Teju", "Tester", "500001")

        checkout2 = CheckoutStepTwo(driver)
        checkout2.click_finish()

        complete = CheckoutComplete(driver)
        assert complete.get_success_message() == "Thank you for your order!"


    @pytest.mark.parametrize("username,password", login_data)
    def test_login_with_excel(self, setup, username, password):

        driver = setup
        logger.info(f"Starting login test for user: {username}")

        login = LoginPage(driver)
        login.login(username, password)

        if username == "standard_user":
            assert "inventory" in driver.current_url
            logger.info("Login successful")
        else:
            assert "error" in driver.page_source
            logger.info("Login failed as expected")