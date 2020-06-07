from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(email, password):
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.get("https://internshala.com/login/user")
    assert "Internships" in driver.title

    elem = driver.find_element_by_xpath('//*[@id="email"]')
    elem.clear()
    elem.send_keys(email)

    elem = driver.find_element_by_xpath('//*[@id="password"]')
    elem.clear()
    elem.send_keys(password)

    elem = driver.find_element_by_xpath('//*[@id="login_submit"]')
    elem.send_keys(password)

login("iamtahirkhan6@gmail.com", "tahir1659456")
