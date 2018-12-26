import json
import requests

link = "https://api-zero.livere.com/v1/comments/list?callback=jQuery1124049866736766120545_1506309304525&limit=10&offset=1&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1506309304527"
headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}

r = requests.get(link, headers=headers)
# print(r.text)

# 获取json的string
json_string = r.text
json_string = json_string[json_string.find('{'):-2]

# json格式解析
json_data = json.loads(json_string)
comment_list = json_data['results']['parents']

for eachone in comment_list:
    message = eachone['content']
    print(message)
    '''
        selenium操控firefox抓取博客评论的时候出现：[WinError 10053] 你的主机中的软件中止了一个已建立的连接， 请大神指点
        刀斯林无处不在
        大巴黎！咚咚咚！
        222333
        111
        为什么第四章出版的时候不重新改改呢
        测试评论
        1111111111111111111111111
        1111111111111111111111111
        哪里哪里在哪里？
    '''


# 批量解析评论
def single_page_comment(link):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    # 获取json的string
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']

    for eachone in comment_list:
        message = eachone['content']
        print(message)


# 爬取前4页的动态评论
for page in range(1, 4):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112407875296433383039_1506267778283&limit=10&offset="
    link2 = "&repSeq=3871836&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1506267778285"
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)
