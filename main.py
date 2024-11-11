from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge()

user_email = input("Please input your email: ")
user_password = input("Please input your password: ")

# First, navigate to the URL
url = "http://app.apollo.io/#/login"
driver.get(url)

try:
    # Define the XPath for the login button and wait for it to appear
    email_textbox_name = "email"
    email_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, email_textbox_name))
    )
    email_input.send_keys(user_email)

    password_textbox_name = "password"
    password_input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, password_textbox_name))
    )
    password_input.send_keys(user_password + Keys.ENTER) 


    time.sleep(10)

except Exception as e:
    print(f"Your exception is {e}")

