from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

'''
    爬取服装网站实例
'''

binary = FirefoxBinary(r"E:\火狐浏览器\firefox.exe")
browser = webdriver.Firefox(firefox_binary=binary, executable_path="D:/geckodriver.exe")
browser.set_page_load_timeout(30)
browser.get('http://www.17huo.com/search.html?sq=2&keyword=%E7%BE%8A%E6%AF%9B')
page_info = browser.find_element_by_css_selector('body > div.wrap > div.pagem.product_list_pager > div')
print(page_info.text)  # 共 100 页，每页 24 条

pages = int((page_info.text.split('，')[0]).split(' ')[1])
print(pages)  # 100

for page in range(pages):
    # 测试只打印第一页
    if page > 0:
        break
    url = 'http://www.17huo.com/?mod=search&sq=2&keyword=%E7%BE%8A%E6%AF%9B&page=' + str(page + 1)
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    goods = browser.find_element_by_css_selector(
        'body > div.wrap > div:nth-child(2) > div.p_main > ul').find_elements_by_tag_name('li')
    print('%d页有%d件商品' % ((page + 1), len(goods)))  # 1页有24件商品
    for good in goods:
        try:
            title = good.find_element_by_css_selector('a:nth-child(1) > p:nth-child(2)').text
            price = good.find_element_by_css_selector('div > a > span').text
            print('success:', title, price)
        except:
            print('expection:', good.text)
'''
    success: 2017年冬季毛呢外套羊毛开衫 ¥140.00
    success: 毛呢外套羊毛单排多扣中长款长袖 ¥135.00
    success: 2017年冬季毛呢外套羊毛长款 ¥120.00
    expection: 小米 有品 90分休闲美利奴羊
    货号：美利奴羊毛袜-OK
    ¥39.00
    云市场（男）供应商-小米 90分-新衣仓
    success: 韩版秋冬毛呢阔腿裤女九分裤羊毛 ¥45.00
    success: 大货已出！红黑格羊毛呢大衣 外 ¥145.00
    success: 超级显瘦【现货】羊毛呢大衣51 ¥135.00
    success: 超级显瘦【现货】羊毛呢大衣51 ¥135.00
    success: 实拍 2017好质量韩版羊毛 ¥145.00
    success: LH LH863 ¥135.00
    success: 羊毛2017年冬季套装/套裙纯 ¥128.00
    success: 毛呢外套西装领韩版百搭气质优雅 ¥175.00
    success: 羊毛2017年冬季套装/套裙纯 ¥128.00
    success: 2017年秋季套装/套裙羊毛双 ¥165.00
    success: 毛呢外套2017年冬季潮流气质 ¥140.00
    success: 2017年冬季毛呢外套韩版百搭 ¥140.00
    success: 毛呢外套V领九分袖中长款宽松休 ¥165.00
    success: 毛呢外套长袖中长款简约口袋甜美 ¥195.00
    success: 毛呢外套长袖中长款简约气质甜美 ¥195.00
    success: 2017年冬季毛呢外套简约口袋 ¥175.00
    success: 气质修身显瘦甜美韩版简约长袖中 ¥185.00
    success: 7280 ¥135.00
    success: 7281 ¥170.00
    success: 7286 ¥145.00
'''
