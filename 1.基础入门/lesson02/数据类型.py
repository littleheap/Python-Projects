import string

# 基本类型
print(type(None))
print(type(True))
print(type(12345))
print(type(123.45))
print(type(1234.))
print(type('abc'))

# 容器类型
print(type([1, 2, 3, 'a', 'bc']))
print(type((1, 2, 3, 'abc')))
values = ['abc', 1, 2, 3.]
print(type(values[3]))
print(type(set(['a', 1, 2.])))
print(type({'a': 123, 4: 'bcd', 5: 'efg'}))


# 函数
def func(): print(100)


print(type(func))

# 模块
print(type(string))


# 自定义类型与类型实例
class Cls: pass


print(type(Cls))
cls = Cls()
print(type(cls))

# 变量赋值
try:
    print(x)  # 变量必须先赋值再使用
except NameError:
    print("NameError: name 'x' is not defined")
x = 100
x = 'abcd'  # x的类型不受限制
