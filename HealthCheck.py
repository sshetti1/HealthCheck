import os
from time import sleep
from selenium import webdriver

def main():
    browser = webdriver.Chrome(executable_path="/chromedriver.exe")
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
