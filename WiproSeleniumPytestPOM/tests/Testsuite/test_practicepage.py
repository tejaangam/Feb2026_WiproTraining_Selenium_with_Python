from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core import driver
from webdriver_manager.firefox import GeckoDriverManager
import time
class Test_practice:

    def test_prac(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        driver.maximize_window()
        time.sleep(2)

        #Radio buttons
        radio1 = driver.find_element(By.XPATH, "//label[@for='radio1']").click()
        time.sleep(2)
        radio2 = driver.find_element(By.XPATH, "//label[@for='radio2']").click()
        time.sleep(2)
        radio3 = driver.find_element(By.XPATH, "//label[@for='radio3']").click()
        time.sleep(2)

        #auto suggest
        auto_suggest = driver.find_element(By.ID, "autocomplete")
        auto_suggest.send_keys("ind")
        time.sleep(2)  # wait for suggestions to load
        # Get all suggestion options
        countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/div")
        # Loop and select India
        for country in countries:
            if country.text == "India":
                country.click()
                break
        time.sleep(2)


        #dropdowns
        dropdown = driver.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
        option1 = driver.find_element(By.XPATH, "//option[text()='Option1']")
        option2 = driver.find_element(By.XPATH, "//option[text()='Option2']")
        option3 = driver.find_element(By.XPATH, "//option[text()='Option3']")
        time.sleep(4)
        #checkboxes
        all_checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
        time.sleep(4)
        #open window and open tab
        open_window = driver.find_element(By.ID, "openwindow")
        driver.close()
        open_tab = driver.find_element(By.ID, "opentab")
        driver.back()
        time.sleep(4)

        #alerts
        alert_btn = driver.find_element(By.ID, "alertbtn")
        confirm_btn = driver.find_element(By.ID, "confirmbtn")
        name_input = driver.find_element(By.ID, "name")
        time.sleep(4)
        #tables- header
        table_header = driver.find_elements(By.XPATH, "//table[@id='product']//th")
        #row
        table_rows = driver.find_elements(By.XPATH, "//table[@id='product']//tr")
        #cell values
        table_cells = driver.find_elements(By.XPATH, "//table[@id='product']//td")
        #Row values
        instructor = driver.find_element(By.XPATH, "//table[@id='product']//td[1]")
        course = driver.find_element(By.XPATH, "//table[@id='product']//td[2]")
        price = driver.find_element(By.XPATH, "//table[@id='product']//td[3]")
        time.sleep(2)
        #hide and show
        showbtn = driver.find_element(By.XPATH, "//input[@id='show-textbox']")
        showbtn.click()
        time.sleep(2)
        hidebtn = driver.find_element(By.XPATH, "//input[@id='hide-textbox']")
        hidebtn.click()
        time.sleep(2)
        #mouse hover
        hover = driver.find_element(By.XPATH, "//button[@id='mousehover']")
        time.sleep(2)
        #iframes
        iframe_element = driver.find_element(By.CSS_SELECTOR, "iframe")
        driver.switch_to.frame(iframe_element)
        driver.switch_to.default_content()
