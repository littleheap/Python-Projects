from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/geckodriver

# 使用Selenium模拟浏览器抓取网页
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r'/Applications/Firefox.app')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

comment = driver.find_element_by_css_selector('div.reply-content')
content = comment.find_element_by_tag_name('p')
print(content.text)

# 加载一页全部评论
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r'/Applications/Firefox.app')
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")
driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))

comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print(content.text)

# 限制图片加载
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
# 把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("permissions.default.image", 2)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")

# 限制 JavaScript 的执行
caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = False
binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
# 把上述地址改成你电脑中Firefox程序的地址
fp = webdriver.FirefoxProfile()
fp.set_preference("javascript.enabled", False)
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp, capabilities=caps)
driver.get("http://www.santostang.com/2017/03/02/hello-world/")
