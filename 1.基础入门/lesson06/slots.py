import traceback

from types import MethodType

'''
    给一个类动态添加属性
'''

class MyClass(object):
    # 限制了添加属性的名字
    __slots__ = ['name', 'set_name']
    # pass

def set_name(self, name):
    self.name = name


cls = MyClass()
cls.name = 'Tom'
# 动态添加方法
cls.set_name = MethodType(set_name, cls)
cls.set_name('Jerry')
print(cls.name)

try:
    cls.age = 30
except AttributeError:
    traceback.print_exc()


# slots对继承类是不限制的
class ExtMyClass(MyClass):
    pass


ext_cls = ExtMyClass()
ext_cls.age = 30
print(ext_cls.age)
