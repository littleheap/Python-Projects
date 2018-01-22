# 按自己定义输出字符串
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        print('print will call __str__ first.')
        return 'Hello ' + self.name + '!'


print(MyClass('Tom'))
