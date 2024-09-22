import os
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

RUN_MODE = "Headless"
# RUN_MODE = "Visible"

# get username and password from credentials.json
with open("credentials.json", "r") as f:
    credentials = json.load(f)

club_uid = credentials["club_uid"]

if RUN_MODE == "Headless":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
else:
    driver = webdriver.Chrome()

try:
    # Login to the website
    driver.get("https://www.fitclub.site/login")
    username_field = driver.find_element(By.ID, "email")
    username_field.send_keys(credentials["username"])
    password_field = driver.find_element(By.ID, "password")  # Modify selector if needed
    password_field.send_keys(credentials["password"] + Keys.ENTER)

    # Wait for login to complete by detecting the user badge "circle-account"
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'circle-account')]"))
    )

    # Navigate to equipment repairs page
    driver.get(f"https://www.fitclub.site/equipment/repairs?clubUid={club_uid}")
    
    time.sleep(0.5)
    
    filter_button = driver.find_element(By.XPATH, "//button[contains(@title, 'Filter')]")
    filter_button.click()
    
    time.sleep(0.5)
    
    checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and @name='filterStatuses']")
    checkboxes[3].click()
    
    filter_go_button = driver.find_element(By.ID, 'myFilterModalCloseButton')
    filter_go_button.click()
    
    time.sleep(0.25)
    
    download_button = driver.find_element(By.XPATH, "//button/span[contains(text(), 'Download')]")
    download_button.click()

finally:
    driver.quit()
    
# Delete the 