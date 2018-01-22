# 动态创建类
def init(self, name):
    self.name = name


def say_hello(self):
    print('Hello, %s!' % self.name)

# type（名字，继承，方法）
# Hello = type('Hello', (object, ), dict(__init__ = init, hello = say_hello))
Hello = type('Hello', (object,), {'__init__': init, 'hello': say_hello})
'''
class Hello:
    def __init__(...)
    def hello(...)
'''
h = Hello('Tom')
h.hello()
