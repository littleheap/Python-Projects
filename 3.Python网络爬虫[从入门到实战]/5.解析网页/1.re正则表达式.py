import re
import requests

# 3种正则表达式

# （1）re.match()
m = re.match('www', 'www.santostang.com')

print("匹配的结果:  ", m)
# 匹配的结果:   <_sre.SRE_Match object; span=(0, 3), match='www'>

print("匹配的起始与终点:  ", m.span())
# 匹配的起始与终点:   (0, 3)

print("匹配的起始位置:  ", m.start())
# 匹配的起始位置:   0

print("匹配的终点位置:  ", m.end())
# 匹配的起始位置:   0

line = "Fat cats are smarter than dogs, is it right?"

m = re.match(r'(.*) are (.*?) dogs', line)

print('匹配的整句话', m.group(0))
# 匹配的整句话 Fat cats are smarter than dogs

print('匹配的第一个结果', m.group(1))
# 匹配的第一个结果 Fat cats

print('匹配的第二个结果', m.group(2))
# 匹配的第二个结果 smarter than

print('匹配的结果列表', m.groups())
# 匹配的结果列表 ('Fat cats', 'smarter than')

# （2）re.search()
m_match = re.match('com', 'www.santostang.com')

m_search = re.search('com', 'www.santostang.com')

print(m_match)
# None

print(m_search)
# <_sre.SRE_Match object; span=(15, 18), match='com'>

# （3）re.findall()
# [0-9]+代表任意长度的数字
m_match = re.match('[0-9]+', '12345 is the first number, 23456 is the sencond')

m_search = re.search('[0-9]+', 'The first number is 12345, 23456 is the sencond')

m_findall = re.findall('[0-9]+', '12345 is the first number, 23456 is the sencond')

print(m_match.group())
# 12345

print(m_search.group())
# 12345

print(m_findall)
# ['12345', '23456']

# 解析网页HTML
link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)
html = r.text

title_list = re.findall('<h1 class="post-title"><a href=.*?>(.*?)</a></h1>', html)

print(html)
'''
    <h1 class="post-title"><a href="http://www.santostang.com/2018/07/15/4-3-%e9%80%9a%e8%bf%87selenium-%e6%a8%a1%e6%8b%9f%e6%b5%8f%e8%a7%88%e5%99%a8%e6%8a%93%e5%8f%96/">4.3 通过selenium 模拟浏览器抓取</a></h1>
'''

print(title_list)
'''
    ['4.3 通过selenium 模拟浏览器抓取', '4.2 解析真实地址抓取', '第四章- 动态网页抓取 (解析真实地址 + selenium)', '《网络爬虫：从入门到实践》一书勘误', 'Hello world!']
'''
