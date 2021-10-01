import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def main():
    options = Options()
    options.binary_location = '/opt/headless-chromium'
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--single-process')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(executable_path='/opt/chromedriver', chrome_options=options)


    browser.get('http://covidcheck.udel.edu/')


    # Click Student/Employee amd ->
    sleep(1)
    studentEmployee = browser.find_element_by_xpath('//*[@id="QID32-4-label"]')
    studentEmployee.click()
    studentButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
    studentButton.click()

    # Username and Password
    sleep(1)
    username = browser.find_element_by_xpath('//*[@id="udelnetid"]')
    username.send_keys(os.getenv("USERNAME"))
    password = browser.find_element_by_xpath('//*[@id="pword"]')
    password.send_keys(os.getenv('PASSWORD'))
    login = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div/div/div[4]/div/button')
    login.click()

    # Welcome Page Next Click
    sleep(1)
    welcomeButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
    welcomeButton.click()

    # Skip Phone Number
    sleep(2)
    phoneButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
    phoneButton.click()

    # Past 2 Weeks
    sleep(2)
    none2Weeks = browser.find_element_by_xpath('//*[@id="QID4-5-label"]')
    none2Weeks.click()
    sleep(1)
    weeksButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
    weeksButton.click()

    # 24 Hours
    sleep(2)
    none24 = browser.find_element_by_xpath('//*[@id="QID6-5-label"]/span')
    none24.click()
    hoursButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
    hoursButton.click()
    sleep(2)

    browser.close()
