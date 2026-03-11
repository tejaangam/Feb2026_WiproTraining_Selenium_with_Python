import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 🔥 Direct banking app link (NO iframe needed)
    driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/")

    WebDriverWait(driver, 10)
    yield driver
    driver.quit()