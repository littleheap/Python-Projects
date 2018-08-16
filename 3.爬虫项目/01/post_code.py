import requests
import xml.etree.ElementTree as ET
from xml.parsers.expat import ParserCreate


class DefaultSaxHandler(object):
    def __init__(self, provinces):
        self.provinces = provinces

    # 处理标签开始
    def start_element(self, name, attrs):
        if name != 'map':
            name = attrs['title']
            number = attrs['href']
            self.provinces.append((name, number))

    # 处理标签结束
    def end_element(self, name):
        pass

    # 文本处理
    def char_data(self, text):
        pass

def get_province_entry(url):
    # 获取文本，并用gb2312解码
    content = requests.get(url).content.decode('gb2312')
    # 确定要查找字符串的开始结束位置，并用切片获取内容。
    start = content.find('<map name=\"map_86\" id=\"map_86\">')
    end = content.find('</map>')
    content = content[start:end + len('</map>')].strip()
    provinces = []
    # 生成Sax处理器
    handler = DefaultSaxHandler(provinces)
    # 初始化分析器
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    # 解析数据
    parser.Parse(content)
    # 结果字典为每一页的入口代码
    return provinces

provinces = get_province_entry('http://www.ip138.com/post')

print(provinces)

'''
[('新疆', '/83/'), ('西藏', '/85/'), ('青海', '/81/'), ('甘肃', '/73/'), ('四川', '/61/'), ('云南', '/65/'), ('宁夏', '/75/'), ('内蒙古', '/01/'), ('黑龙江', '/15/'), ('吉林', '/13/'), ('辽宁', '/11/'), ('河北', '/50/'), ('北京', '/10/'), ('天津', '/30/'), ('陕西', '/71/'), ('山西', '/03/'), ('山东', '/25/'), ('河南', '/45/'), ('重庆', '/40/'), ('湖北', '/43/'), ('安徽', '/23/'), ('江苏', '/21/'), ('上海', '/20/'), ('贵州', '/55/'), ('广西', '/53/'), ('湖南', '/41/'), ('江西', '/33/'), ('浙江', '/31/'), ('福建', '/35/'), ('广东', '/51/'), ('海南', '/57/'), ('台湾', '/taiwang/'), ('澳门', '/aomen/'), ('香港', '/xianggang/')]
'''
