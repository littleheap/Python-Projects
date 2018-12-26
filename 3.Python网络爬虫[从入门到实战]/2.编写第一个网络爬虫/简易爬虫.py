import requests

# 1.获取页面
link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers=headers)
# print(r.text)  # 打印了整个页面HTML源码

# 2.提取需要的数据
from bs4 import BeautifulSoup  # 从bs4这个库中导入BeautifulSoup

soup = BeautifulSoup(r.text, "html.parser")  # 使用BeautifulSoup解析这段代码
title = soup.find("h1", class_="post-title").a.text.strip()  # 抓取博客页面第一篇文章标题
print(title)  # 打印标题：4.3 通过selenium 模拟浏览器抓取

# 3.存储数据
with open('title_test.txt', "a+") as f:
    f.write(title)
    f.close()
