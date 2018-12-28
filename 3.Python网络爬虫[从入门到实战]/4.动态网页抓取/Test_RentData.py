import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'D:\Program Files\Mozilla Firefox\firefox.exe')
# 把上述地址改成你电脑中Firefox程序的地址

# 用 selenium 的 driver 来启动 firefox
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
# 在虚拟浏览器中打开 Airbnb 页面
driver.get("https://zh.airbnb.com/s/Shenzhen--China?page=1")

for i in range(0, 5):
    # 找到页面中所有的出租房
    rent_list = driver.find_elements_by_css_selector('div._1788tsr0')

    # 对于每一个出租房
    for eachhouse in rent_list:
        # 找到评论数量
        try:
            comment = eachhouse.find_element_by_css_selector('span._gb7fydm')
            comment = comment.text
        except:
            comment = 0

        # 找到价格
        price = eachhouse.find_element_by_css_selector('span._hylizj6')
        price = price.text[4:]

        # 找到名称
        name = eachhouse.find_element_by_css_selector('div._ew0cqip')
        name = name.text

        # 找到房屋类型，大小
        details = eachhouse.find_elements_by_css_selector('div._saba1yg small div span')
        details = details[0].text
        house_type = details.split(" · ")[0]
        bed_number = details.split(" · ")[1]
        print(comment, price, name, house_type, bed_number)
    # 下一页
    nextpage = driver.find_element_by_css_selector('li._b8vexar').click()
    time.sleep(5)
