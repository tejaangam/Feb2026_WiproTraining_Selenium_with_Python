import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_scroll:
    def test_scroll(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.amazon.in/')
        #amz = driver.find_element(By.XPATH, "//a[normalize-space()='Amazon Pay on Merchants']")
        #driver.execute_script("arguments[0].scrollIntoView();", amz)
        time.sleep(2)
        #amz.click()

        #vertical up scroll - x coordinates should be zero
        driver.execute_script("window.scrollBy(0, -1000)")

        #vertical down scroll
        driver.execute_script("window.scrollBy(0, 1000)")

        driver.quit()





