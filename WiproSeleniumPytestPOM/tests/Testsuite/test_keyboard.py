import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_dd:
    def test_dd(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

        driver.get("https://www.facebook.com/")
        driver.maximize_window()
        time.sleep(2)

        actions = ActionChains(driver)
        email = driver.find_element(By.XPATH, "//input[@name='']")
        seriesofactions  = (actions.move_to_element(email).key_down(Keys.SHIFT).send_keys("hello")
                            .key_up(Keys.SHIFT)
                            .key_down(Keys.CONTROL)
                            .send_keys('a')
                            .send_keys('c')
                            .key_up(Keys.CONTROL)
                            .key_down(Keys.TAB)
                            .key_down(Keys.CONTROL)
                            .send_keys('v')
                            .key_up(Keys.CONTROL)
                            .key_down(Keys.TAB)
                            .key_down(Keys.ENTER))
        seriesofactions.perform()
        time.sleep(3)
        driver.close()