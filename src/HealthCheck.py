from time import sleep

from selenium import webdriver

browser = webdriver.Chrome(executable_path="C:/Users/got2b/Documents/Random Code/HealthCheck/chromedriver.exe")
browser.get('http://covidcheck.udel.edu/')
sleep(2)

#Click Student/Employee amd ->
studentEmployee = browser.find_element_by_xpath('//*[@id="QID32-4-label"]')
studentEmployee.click()
nextButton = browser.find_element_by_xpath('//*[@id="NextButton"]')
nextButton.click()
