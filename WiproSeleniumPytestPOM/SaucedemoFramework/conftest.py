import datetime
import os
from datetime import datetime
import pytest
from utils.utilities import get_driver

@pytest.fixture
def setup(driver):
    driver = get_driver()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)