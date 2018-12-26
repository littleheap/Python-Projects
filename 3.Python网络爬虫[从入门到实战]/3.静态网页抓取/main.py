import requests

# 请求页面
r = requests.get('http://www.santostang.com/')

# 输出获取的信息
print("文本编码:", r.encoding)  # 文本编码: UTF-8
print("响应状态码:", r.status_code)  # 200表示请求成功 响应状态码: 200
# print("字符串方式的响应体:", r.text)

# 传递URL参数
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=key_dict)

print("URL已经正确编码:", r.url)  # URL已经正确编码: http://httpbin.org/get?key1=value1&key2=value2
print("字符串方式的响应体: \n", r.text)
'''
    字符串方式的响应体: 
     {
      "args": {
        "key1": "value1", 
        "key2": "value2"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.21.0"
      }, 
      "origin": "111.166.36.3", 
      "url": "http://httpbin.org/get?key1=value1&key2=value2"
    }
'''

# 定制请求头
# 去页面信息查找页面对应的Header请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
    'Host': 'www.santostang.com'
}
r = requests.get('http://www.santostang.com/', headers=headers)
print("响应状态码:", r.status_code)  # 响应状态码: 200

# 发送POST请求
key_dict = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=key_dict)
print("URL已经正确编码:", r.url)  # URL已经正确编码: http://httpbin.org/post
print(r.text)
'''
    {
      "args": {}, 
      "data": "", 
      "files": {}, 
      "form": {
        "key1": "value1", 
        "key2": "value2"
      }, 
      "headers": {
        "Accept": "*/*", 
        "Accept-Encoding": "gzip, deflate", 
        "Connection": "close", 
        "Content-Length": "23", 
        "Content-Type": "application/x-www-form-urlencoded", 
        "Host": "httpbin.org", 
        "User-Agent": "python-requests/2.21.0"
      }, 
      "json": null, 
      "origin": "111.166.36.3", 
      "url": "http://httpbin.org/post"
    }
'''

# 超时处理
link = "http://www.santostang.com/"
r = requests.get(link, timeout=0.001)
