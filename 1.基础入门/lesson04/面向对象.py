# 创建类
class Foo:
    # 类中的函数
    def bar(self):
        # 功能阐述
        pass


# =====完毕========

# 根据Foo创建对象obj
obj = Foo()

print("-----------------------")


# 创建对象的时候 记得后面加个括号

# 创建类
class Foo:
    def bar(self):
        print('Bar')

    def hello(self, name):
        print('i am %s' % name)


# 根据Foo创建的对象
obj = Foo()
obj.bar()  # 执行Bar方法
obj.hello('july')  # 执行Hello方法　

print("-----------------------")


# 创建类
class Foo:
    # 这里我们可以创建一个类级别的变量
    # 它不会随着由此类创建的变量而变化
    name = 'Jan'

    def bar(self):
        print('Bar')

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# 根据Foo创建的对象
obj1 = Foo()
obj2 = Foo()
obj1.hello('August')
obj2.hello('July')

print("-----------------------")


# 创建类
class Foo:
    # 这里我们可以创建一个类级别的变量
    # 它不会随着由此类创建的变量而变化
    name = 'Jan'

    def bar(july):
        print('Bar')

    def hello(july, name):  # 我这里把self改成了july，
        # 但是只要它作为第一参数的位置没变，它依旧是Foo Class的自我指代
        print('you are %s' % july.name)
        print('I am %s' % name)
        print('\n')


# 根据Foo创建的对象
obj1 = Foo()
obj2 = Foo()
obj1.hello('August')
obj2.hello('July')

print("-----------------------")


# 创建类
class Foo:
    def __init__(self):
        # 这就是构造函数，它的职责是在模型创建的初期，就完成一些动作
        # 简单的说就是，自定义的初始化步骤：
        # 同样，它需要self来指代本身这个class
        self.name = 'Jan'

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# ==== 完毕 =====

# 当你创建一个Foo类的时候，init会被自动跑一遍：
obj = Foo()
# 在我们的例子中，我们默认给self自己的name变量，赋值为’JAN‘
# 此刻，当我们调用Foo的hello()方法时，hello自己的name变量，被赋值为'July'
obj.hello('July')

print("-----------------------")


# 创建类
class Foo:
    def __init__(self, name2):
        # 你可以在这里附加上一些参数
        # 这些参数将是你创建一个Foo类时的必要条件
        self.name = name2

    def hello(self, name):
        print('you are %s' % self.name)
        print('I am %s' % name)
        print('\n')


# ==== 完毕 =====

# 当你创建一个Foo类的时候，init会被自动跑一遍：
# 此刻，你不可以直接跑Foo(),你需要填入一个参数：name2
obj = Foo('Feb')
# 然后再调用hello, 并赋值July
obj.hello('July')

print("-----------------------")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


LiLei = Student('LiLei', 12)
LiLei.age = 20
LiLei.detail()

print("-----------------------")


class Student:
    def __init__(self, name, age):
        # 不可篡改
        self.__name = name
        self.__age = age

    def detail(self):
        print(self.__name)
        print(self.__age)


LiLei = Student('LiLei', 12)
LiLei.__age = 20
LiLei.detail()

print("-----------------------")


# Get&Set方法访问
class Student(object):
    ...

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Student(object):
    ...

    def set_age(self, age):
        self.__age = age


print("-----------------------")


class Student:
    # 假定我们初始化一个Student类的时候要做的就是，记录下每个学生的名字和年龄
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # 至此，我们用self指代student本身，并用name和age存下了他们的年龄和名字

        # === 完毕 ===


# 此时，我们新建一个学生
obj1 = Student('July', 18)
print(obj1.name)  # 直接调用obj1对象的name属性
print(obj1.age)  # 直接调用obj1对象的age属性
obj2 = Student('Aug', 73)
print(obj2.name)  # 直接调用obj2对象的name属性
print(obj2.age)  # 直接调用obj2对象的age属性

print("-----------------------")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)

        # === 完毕 ===


# 此时，我们新建一个学生
obj1 = Student('July', 18)
obj1.detail()  # Python默认将obj1传给self，所以其实我们做的是obj1.detail(obj1)
# 那么，detail()内部的样貌其实就是：
# print(obj1.name)
# print(obj1.age)
obj2 = Student('Aug', 73)
obj2.detail()

print("-----------------------")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def detail(self):
        print(self.name)
        print(self.age)


class PrimaryStudent(Student):
    def lol(self):
        print('不服solo！')


class CollegeStudent(Student):
    def __init__(self, name, age, gf):
        self.name = name
        self.age = age
        self.gf = gf

    def gf_detail(self):
        print(self.gf)


obj1 = PrimaryStudent('小王', 7)
obj1.lol()
obj1.detail()

obj2 = CollegeStudent('王思聪', 29, '张雨馨')
obj2.detail()
obj2.gf_detail()

print("-----------------------")


# 经典类的写法
class c1:
    pass


class c2(c1):
    pass


# 新类的写法
class N1(object):
    pass


class N2(N1):
    pass


print("-----------------------")


class D:
    def bar(self):
        print('D.bar')


class C(D):
    def bar(self):
        print('C.bar')


class B(D):
    pass


class A(B, C):
    pass


a = A()
# 执行bar方法时
# 首先去A类中查找，如果A类中没有，则继续去B类中找，如果B类中没有，则继续去D类中找，如果D类中没有，则继续去C类中找，如果还是未找到，则报错
# 所以，查找顺序：A --> B --> D --> C
# 在上述查找bar方法的过程中，一旦找到，则寻找过程立即中断，便不会再继续找了
a.bar()

print("-----------------------")


class F1:
    pass


class S1(F1):
    def show(self):
        print('S1.show')


class S2:
    def show(self):
        print('S2.show')


def Func(obj):
    """Func函数需要接收一个F1类型或者F1子类的类型"""
    obj.show()


s1_obj = S1()
Func(s1_obj)  # 在Func函数中传入S1类的对象 s1_obj，执行 S1 的show方法，结果：S1.show

s2_obj = S2()
Func(s2_obj)  # 在Func函数中传入Ss类的对象 ss_obj，执行 Ss 的show方法，结果：S2.show

print("-----------------------")


# isinstance()可以告诉我们，一个对象是否是某种类型（包括继承关系）。

class A:
    pass


class B(A):
    pass


class C(B):
    pass


k = A()
g = B()
y = C()

print(isinstance(y, C))

print("-----------------------")

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir('ABC'))

print("-----------------------")


class MyObject:
    def __len__(self):
        return 100


obj = MyObject()
len(obj)


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject:
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

# 紧接着，可以测试该对象的属性：

hasattr(obj, 'x')  # 有木有属性'x'

hasattr(obj, 'y')  # 有属性'y'吗？

setattr(obj, 'y', 19)  # 设置一个属性'y'

hasattr(obj, 'y')  # 有属性'y'吗？

getattr(obj, 'y')  # 获取属性'y'

# 可以传入一个default参数，如果属性不存在，就返回默认值：

getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404

# 也可以获得对象的方法：

hasattr(obj, 'power')  # 有属性'power'吗？

getattr(obj, 'power')  # 获取属性'power'

fn = getattr(obj, 'power')  # 获取属性'power'并赋值到变量fn

fn  # fn指向obj.power
