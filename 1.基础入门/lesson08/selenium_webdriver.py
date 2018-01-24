from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''
    webdriver登录github
'''
binary = FirefoxBinary(r"E:\FireFox\firefox.exe")

browser = webdriver.Firefox(firefox_binary=binary, executable_path="D:/geckodriver.exe")

browser.get('http://github.com/login')

element_user = browser.find_element_by_id('login_field')

element_user.send_keys('')

element_password = browser.find_element_by_id('password')

element_password.send_keys('')

element_password.submit()
