import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def HealthCheck():
    ser = Service(ChromeDriverManager().install())
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=ser, chrome_options=chrome_options)

    browser.get('http://covidcheck.udel.edu/')


    # Click Student/Employee amd ->
    sleep(5)
    studentEmployee = browser.find_element(By.XPATH, '//*[@id="QID32-4-label"]')
    studentEmployee.click()
    studentButton = browser.find_element(By.XPATH, '//*[@id="NextButton"]')
    studentButton.click()

    # Username and Password
    sleep(5)
    username = browser.find_element(By.XPATH, '//*[@id="udelnetid"]')
    username.send_keys(os.getenv("USERNAME"))
    password = browser.find_element(By.XPATH, '//*[@id="pword"]')
    password.send_keys(os.getenv('PASSWORD'))
    login = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/form/div/div/div[4]/div/button')
    login.click()

    # Welcome Page Next Click
    sleep(5)
    welcomeButton = browser.find_element(By.XPATH, '//*[@id="NextButton"]')
    welcomeButton.click()

    # Skip Phone Number
    sleep(5)
    phoneButton = browser.find_element(By.XPATH, '//*[@id="NextButton"]')
    phoneButton.click()

    # Past 2 Weeks
    sleep(5)
    none2Weeks = browser.find_element(By.XPATH, '//*[@id="QID4-5-label"]')
    none2Weeks.click()
    sleep(5)
    weeksButton = browser.find_element(By.XPATH, '//*[@id="NextButton"]')
    weeksButton.click()

    # 24 Hours
    sleep(5)
    none24 = browser.find_element(By.XPATH, '//*[@id="QID6-5-label"]/span')
    none24.click()
    hoursButton = browser.find_element(By.XPATH, '//*[@id="NextButton"]')
    hoursButton.click()
    sleep(5)

    browser.close()


HealthCheck()
