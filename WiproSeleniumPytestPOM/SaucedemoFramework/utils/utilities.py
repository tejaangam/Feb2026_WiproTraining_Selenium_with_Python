from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():

    options = webdriver.ChromeOptions()

    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.maximize_window()
    driver.implicitly_wait(10)

    return driver