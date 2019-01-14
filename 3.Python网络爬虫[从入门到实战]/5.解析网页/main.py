import re
import requests
from bs4 import BeautifulSoup

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

# 使用BeautifulSoup抓取标题
link = "http://www.santostang.com/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers=headers)

soup = BeautifulSoup(r.text, "html.parser")
first_title = soup.find("h1", class_="post-title").a.text.strip()
print("第一篇文章的标题是：", first_title)
# 第一篇文章的标题是： 4.3 通过selenium 模拟浏览器抓取

title_list = soup.find_all("h1", class_="post-title")
for i in range(len(title_list)):
    title = title_list[i].a.text.strip()
    print('第 %s 篇文章的标题是：%s' % (i + 1, title))
    '''
        第 1 篇文章的标题是：4.3 通过selenium 模拟浏览器抓取
        第 2 篇文章的标题是：4.2 解析真实地址抓取
        第 3 篇文章的标题是：第四章- 动态网页抓取 (解析真实地址 + selenium)
        第 4 篇文章的标题是：《网络爬虫：从入门到实践》一书勘误
        第 5 篇文章的标题是：Hello world!
    '''

# 使用BeautifulSoup进行代码美化
html = """
<body>
<header id="header">
    <h3 id="name">大数据@唐松Santos</h3>
  <div class="sns">
    <a href="http://www.santostang.com/feed/" target="_blank" rel="nofollow" title="RSS"><i class="fa fa-rss" aria-hidden="true"></i></a>
        <a href="http://weibo.com/santostang" target="_blank" rel="nofollow" title="Weibo"><i class="fa fa-weibo" aria-hidden="true"></i></a>
                <a href="https://www.linkedin.com/in/santostang" target="_blank" rel="nofollow" title="Linkedin"><i class="fa fa-linkedin" aria-hidden="true"></i></a>
                <a href="mailto:tangsongsky@gmail.com" target="_blank" rel="nofollow" title="envelope"><i class="fa fa-envelope" aria-hidden="true"></i></i></a>
          </div>
  <div class="nav">
   <ul><li class="current-menu-item"><a href="http://www.santostang.com/">首页</a></li>
<li><a href="http://www.santostang.com/about-me/">关于我</a></li>
<li><a href="http://www.santostang.com/post-search/">文章搜索</a></li>
<li><a href="http://www.santostang.com/wp-login.php">登录</a></li>
</ul>  </div>
</header>
"""
soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())
'''
    <body>
     <header id="header">
      <h3 id="name">
       大数据@唐松Santos
      </h3>
      <div class="sns">
       <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS">
        <i aria-hidden="true" class="fa fa-rss">
        </i>
       </a>
       <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo">
        <i aria-hidden="true" class="fa fa-weibo">
        </i>
       </a>
       <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin">
        <i aria-hidden="true" class="fa fa-linkedin">
        </i>
       </a>
       <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope">
        <i aria-hidden="true" class="fa fa-envelope">
        </i>
       </a>
      </div>
     </header>
    </body>
    <div class="nav">
     <ul>
      <li class="current-menu-item">
       <a href="http://www.santostang.com/">
        首页
       </a>
      </li>
      <li>
       <a href="http://www.santostang.com/about-me/">
        关于我
       </a>
      </li>
      <li>
       <a href="http://www.santostang.com/post-search/">
        文章搜索
       </a>
      </li>
      <li>
       <a href="http://www.santostang.com/wp-login.php">
        登录
       </a>
      </li>
     </ul>
    </div>
'''

print(soup.header.h3)
# <h3 id="name">大数据@唐松Santos</h3>

print(soup.header.div.contents)
'''
    ['\n', <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>, '\n', <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo"><i aria-hidden="true" class="fa fa-weibo"></i></a>, '\n', <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin"><i aria-hidden="true" class="fa fa-linkedin"></i></a>, '\n', <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope"><i aria-hidden="true" class="fa fa-envelope"></i></a>]
'''

print(soup.header.div.contents[1])
'''
    <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
'''

for child in soup.header.div.children:
    print(child)
    '''
        <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
    
    
        <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
        
        
        <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo"><i aria-hidden="true" class="fa fa-weibo"></i></a>
        
        
        <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin"><i aria-hidden="true" class="fa fa-linkedin"></i></a>
        
        
        <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope"><i aria-hidden="true" class="fa fa-envelope"></i></a>
    '''

for child in soup.header.div.descendants:
    print(child)
    '''
        <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
        <i aria-hidden="true" class="fa fa-rss"></i>
        
        
        <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo"><i aria-hidden="true" class="fa fa-weibo"></i></a>
        <i aria-hidden="true" class="fa fa-weibo"></i>
        
        
        <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin"><i aria-hidden="true" class="fa fa-linkedin"></i></a>
        <i aria-hidden="true" class="fa fa-linkedin"></i>
        
        
        <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope"><i aria-hidden="true" class="fa fa-envelope"></i></a>
        <i aria-hidden="true" class="fa fa-envelope"></i>
    '''

a_tag = soup.header.div.a
print(a_tag)
# <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
print(a_tag.parent)
'''
    <div class="sns">
    <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
    <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo"><i aria-hidden="true" class="fa fa-weibo"></i></a>
    <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin"><i aria-hidden="true" class="fa fa-linkedin"></i></a>
    <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope"><i aria-hidden="true" class="fa fa-envelope"></i></a></div>
'''

print(soup.find_all('div', class_='sns'))
'''
    [<div class="sns">
    <a href="http://www.santostang.com/feed/" rel="nofollow" target="_blank" title="RSS"><i aria-hidden="true" class="fa fa-rss"></i></a>
    <a href="http://weibo.com/santostang" rel="nofollow" target="_blank" title="Weibo"><i aria-hidden="true" class="fa fa-weibo"></i></a>
    <a href="https://www.linkedin.com/in/santostang" rel="nofollow" target="_blank" title="Linkedin"><i aria-hidden="true" class="fa fa-linkedin"></i></a>
    <a href="mailto:tangsongsky@gmail.com" rel="nofollow" target="_blank" title="envelope"><i aria-hidden="true" class="fa fa-envelope"></i></a></div>]
'''

# 文档搜索树
for tag in soup.find_all(re.compile("^h")):
    print(tag.name)
    '''
        header
        h3
    '''
