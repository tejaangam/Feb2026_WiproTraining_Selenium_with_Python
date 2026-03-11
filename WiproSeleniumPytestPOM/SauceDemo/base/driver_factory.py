# SauceDemo/base/driver_factory.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class DriverFactory:

    @staticmethod
    def get_driver():
        chrome_options = Options()

        # Disable password manager & breach detection
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        chrome_options.add_experimental_option("prefs", prefs)

        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--disable-save-password-bubble")
        chrome_options.add_argument("--incognito")

        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chrome_options
        )

        driver.maximize_window()
        return driver