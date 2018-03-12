from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

'''
    webdriver登录github
'''

'''
binary = FirefoxBinary(r"E:\火狐浏览器\firefox.exe")

browser = webdriver.Firefox(firefox_binary=binary, executable_path="D:/geckodriver.exe")

browser.get('http://github.com/login')

element_user = browser.find_element_by_id('login_field')

element_user.send_keys('littleheap')

element_password = browser.find_element_by_id('password')

element_password.send_keys('waim321123asdf')

element_password.submit()
'''

binary = FirefoxBinary(r"E:\火狐浏览器\firefox.exe")

browser = webdriver.Firefox(firefox_binary=binary, executable_path="D:/geckodriver.exe")

browser.get('http://my.csu.edu.cn/login/index.jsp')

element_user = browser.find_element_by_id('userId')

element_user.send_keys('0902150211')

element_password = browser.find_element_by_id('pwd')

element_password.send_keys('86161145')

login = browser.find_element_by_class_name('js_btn')

login.click()

# 进入个人主页
