import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_google_workflow(browser):

    # 1 Open browser and verify page title
    browser.get("https://www.google.com")
    assert "Google" in browser.title

    # 2 Search for “Robot Framework”
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("Robot Framework")
    search_box.send_keys(Keys.RETURN)

    # 3 Click a link and verify URL
    browser.find_element(By.PARTIAL_LINK_TEXT, "Robot Framework").click()
    assert "robotframework" in browser.current_url.lower()

    # 4 Enter text into input field and validate value
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.clear()
    search_box.send_keys("Automation Testing")

    # Validate entered text
    entered_value = search_box.get_attribute("value")
    assert entered_value == "Automation Testing"