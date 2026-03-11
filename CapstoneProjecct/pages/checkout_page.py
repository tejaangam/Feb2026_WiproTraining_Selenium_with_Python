from selenium.webdriver.common.by import By
from pages.basepage import BasePage
from utilities.logger import get_logger

logger = get_logger()


class CheckoutPage(BasePage):

    first_name = (By.ID, "firstNameInput")
    last_name = (By.ID, "lastNameInput")
    address = (By.ID, "addressLine1Input")
    province = (By.ID, "provinceInput")
    postal = (By.ID, "postCodeInput")
    continue_btn = (By.ID, "checkout-shipping-continue")

    download_receipt_btn = (By.ID, "downloadpdf")

    def enter_shipping_details(self, firstname, lastname, address, city, state, zipcode):

        try:

            logger.info("Entering shipping details")
            self.type(self.first_name, firstname)
            self.type(self.last_name, lastname)
            self.type(self.address, address)
            self.type(self.province, city)
            self.type(self.postal, str(zipcode))

            logger.info("Clicking continue button")

            self.click(self.continue_btn)

        except Exception as e:

            logger.error("Shipping details failed: " + str(e))
            raise

    def download_receipt(self):

        try:

            logger.info("Downloading receipt")

            self.click(self.download_receipt_btn)

        except Exception as e:

            logger.error("Receipt download failed: " + str(e))
            raise