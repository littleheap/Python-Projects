import json
import requests

from PIL import Image
from io import BytesIO

# print(dir(requests))
# ['BytesIO', 'Image', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'json', 'requests']


url = 'http://www.baidu.com'
r = requests.get(url)
# print(r.text)
'''
<!DOCTYPE html>
<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>ç¾åº¦ä¸ä¸ï¼ä½ å°±ç¥é</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=ç¾åº¦ä¸ä¸ class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>æ°é»</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>å°å¾</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>è§é¢</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>è´´å§</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>ç»å½</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">ç»å½</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ´å¤äº§å</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>å³äºç¾åº¦</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>ä½¿ç¨ç¾åº¦åå¿è¯»</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>æè§åé¦</a>&nbsp;äº¬ICPè¯030173å·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>
'''
print(r.status_code)  # 200
print(r.encoding)  # ISO-8859-1

# 传递参数
# params = {'k1': 'v1', 'k2': 'v2'}
# r = requests.get('http://httpbin.org/get', params)
# print(r.url)

# 二进制数据
# r = requests.get('http://i-2.shouji56.com/2015/2/11/23dab5c5-336d-4686-9713-ec44d21958e3.jpg')
# image = Image.open(BytesIO(r.content))
# image.save('meinv.jpg')

# json处理
r = requests.get('https://github.com/timeline.json')
print(type(r.json))  # <class 'method'>
print(r.text)
'''
{"message":"Hello there, wayfaring stranger. If you’re reading this then you probably didn’t see our blog post a couple of years back announcing that this API would go away: http://git.io/17AROg Fear not, you should be able to get what you need from the shiny new Events API instead.","documentation_url":"https://developer.github.com/v3/activity/events/#list-public-events"}
'''

# 原始数据处理
# r = requests.get('http://i-2.shouji56.com/2015/2/11/23dab5c5-336d-4686-9713-ec44d21958e3.jpg', stream=True)
# with open('meinv2.jpg', 'wb+') as f:
#     for chunk in r.iter_content(1024):
#         f.write(chunk)

# 提交表单
# form = {'username': 'user', 'password': 'pass'}
# r = requests.post('http://httpbin.org/post', data=form)
# print(r.text)
# r = requests.post('http://httpbin.org/post', data=json.dumps(form))
# print(r.text)

# cookie
url = 'http://www.baidu.com'
r = requests.get(url)
cookies = r.cookies
for k, v in cookies.get_dict().items():
    print(k, v)  # BDORZ 27315

cookies = {'c1': 'v1', 'c2': 'v2'}
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.text)
'''
    {
      "cookies": {
        "c1": "v1", 
        "c2": "v2"
      }
    }   
'''

# 重定向和重定向历史
r = requests.head('http://github.com', allow_redirects=True)
print(r.url)  # https://github.com/
print(r.status_code)  # 200
print(r.history)  # (<Response [301]>,)

# 代理
# proxies = {'http': ',,,', 'https': '...'}
# r = requests.get('...', proxies=proxies)
