import webdriver_manager
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import title_is

from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_Google():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://google.com')
    assert driver.title== "Google"

    driver.maximize_window()

    driver.quit()

def test_login_facebook():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.implicitly_wait(10)
    driver.get('https://facebook.com')
    assert driver.title == "Facebook – log in or sign up"

    driver.maximize_window()

    driver.quit()

def test_login_gmail():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.get('https://gmail.com')
    assert driver.title == "Gmail"

    driver.maximize_window()

    driver.quit()



    # Locate username and password fields
    #username_field = driver.find_element(By.ID, "username")  # Adjust the locator as needed
   # password_field = driver.find_element(By.ID, "password