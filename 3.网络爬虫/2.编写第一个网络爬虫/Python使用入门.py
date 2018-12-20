# 基本命令

print("Hello World!")  # Hello World!

x = 1
if x == 1:
    print("Hello World!")  # Hello World!

# 在前面加上#，代表注释
print("Hello World!")  # Hello World!

# 数据类型

string1 = 'Python Web Scrappy'
string2 = "by Santos"
string3 = string1 + " " + string2
print(string3)  # Python Web Scrappy by Santos

int1 = 7
float1 = 7.5
trans_int = int(float1)
print(trans_int)  # 7

list1 = ['Python', 'Web', 'Scrappy']
list2 = [1, 2, 3, 4, 5]
list3 = ["a", 2, "c", 4]
print("list1[0]: ", list1[0])  # list1[0]:  Python
print("list2[1:3]: ", list2[1:3])  # list2[1:3]:  [2, 3]

list1[1] = "new"
print(list1)  # ['Python', 'new', 'Scrappy']

namebook = {"Name": "Alex", "Age": 7, "Class": "First"}
print(namebook["Name"])  # 可以把相应的键值放入方括号，提取值Alex
print(namebook)  # 也可以直接输出整个字典{'Name': 'Alex', 'Age': 7, 'Class': 'First'}

# 循环提取整个dictionary的key和value
for key, value in namebook.items():
    print(key, value)
    '''
        Name Alex
        Age 7
        Class First
    '''

# 条件语句和循环语句

book = "python"  # 定义字符串book
if book == "python":  # 判断变量是否为'python'
    print("You are studying python.")  # 条件成立时输出You are studying python.
else:
    print("Wrong.")  # 条件不成立时输出

book = "java"  # 定义字符串book
if book == "python":  # 判断变量是否为'python'
    print("You are studying python.")  # 条件成立时输出
elif book == "java":  # 判断变量是否为'java '
    print("You are studying java.")  # 条件成立时输出You are studying java.
else:
    print("Wrong.")  # 条件不成立时输出

citylist = ["Beijing", "Shanghai", "Guangzhou"]
for eachcity in citylist:
    print(eachcity)
    '''
        Beijing
        Shanghai
        Guangzhou
    '''

count = 0
while count < 3:
    print(count)  # 打印出 0,1,2
    count += 1  # 与 count = count + 1 一样


# 函数

# 定义函数
def calulus(x):
    y = x + 1
    return y


# 调用函数
result = calulus(2)
print(result)  # 3


# 定义函数
def fruit_function(fruit1, fruit2):
    fruits = fruit1 + " " + fruit2
    return fruits


# 调用函数
result = fruit_function("apple", "banana")
print(result)  # apple banana


# 面向对象编程

class Person:  # 创建类
    def __init__(self, name, age):  # __init__()方法称为类的构造方法
        self.name = name
        self.age = age

    def detail(self):  # 通过self调用被封装的内容
        print(self.name)
        print(self.age)


obj1 = Person('santos', 18)
obj1.detail()  # Python将obj1传给self参数，即：obj1.detail(obj1)，此时内部self＝obj1
'''
    santos
    18
'''


def detail(name, age):
    print(name)
    print(age)


obj1 = detail('santos', 18)
'''
    santos
    18
'''


class Person:  # 创建类
    def __init__(self, name, age):  # __init__()方法称为类的构造方法
        self.name = name
        self.age = age


obj1 = Person('santos', 18)  # 将"santos"和 18 分别封装到 obj1 及 self的 name和age属性


# 封装
class Person:  # 创建类
    def __init__(self, name, age):  # __init__()方法称为类的构造方法
        self.name = name
        self.age = age


obj1 = Person('santos', 18)  # 将"santos"和 18 分别封装到 obj1 及 self的 name和age属性
print(obj1.name)  # 直接调用obj1对象的name属性santos
print(obj1.age)  # 直接调用obj1对象的age属性18


class Person:  # 创建类
    def __init__(self, name, age):  # __init__()方法称为类的构造方法
        self.name = name
        self.age = age

    def detail(self):  # 通过self调用被封装的内容
        print(self.name)
        print(self.age)


obj1 = Person('santos', 18)
obj1.detail()  # Python将obj1传给self参数，即：obj1.detail(obj1)，此时内部self＝obj1


# 继承
class Animal:
    def eat(self):
        print("%s 吃 " % self.name)

    def drink(self):
        print("%s 喝 " % self.name)

    def shit(self):
        print("%s 拉 " % self.name)

    def pee(self):
        print("%s 撒 " % self.name)


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('喵喵叫')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def cry(self):
        print('汪汪叫')


c1 = Cat('小白家的小黑猫')
c1.eat()  # 小白家的小黑猫 吃
c1.cry()  # 喵喵叫

d1 = Dog('胖子家的小瘦狗')
d1.eat()  # 胖子家的小瘦狗 吃
