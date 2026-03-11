import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


class Test_actions:
    def test_scroll(self):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        driver.maximize_window()
        driver.get('https://www.amazon.in/')
        time.sleep(2)

        actions = ActionChains(driver)
        time.sleep(3)
        bestsellers = driver.find_element(By.XPATH, "//a[normalize-space()='Bestsellers']")
        actions.double_click(bestsellers).perform() #double click
        time.sleep(2)
        driver.back()
        time.sleep(2)
        mobiles = driver.find_element(By.XPATH, "//a[normalize-space()='Mobiles']")
        actions.context_click().perform() #right click
        time.sleep(2)
        driver.back()

        #move to element
        prime = driver.find_element(By.XPATH, "//span[normalize-space()='Prime']")
        actions.move_to_element(prime).perform()
        time.sleep(2)
        #click and hold
        fresh = driver.find_element(By.XPATH, "//a[contains(@href,'/fresh?ref_=nav_cs_grocery')]")
        actions.click_and_hold(fresh).perform()
        driver.quit()




