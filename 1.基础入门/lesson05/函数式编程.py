'''
    可以把别的函数作为参数传入的函数叫高阶函数
'''

print(abs(-10))

f = abs
print(f(-10))


def add(x, y, f):
    return f(x) + f(y)


print(add(-10, -5, abs))
print(add(-10, -5, f))

'''
    匿名函数：
    python 使用 lambda 来创建匿名函数
    lambda只是一个表达式，函数体比def简单很多
    lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率
    最重要的一点，Lambda表达式可以体现你的逼格。华尔街和伦敦银行高街最逼的一群人都是自诩用且只用函数式编程的
    什么是函数式编程？就是类似于全篇程序都用python中lambda这样的一行代码来解决问题
'''

sum = lambda arg1, arg2: arg1 + arg2

print(sum(10, 20))

from functools import reduce

# 这里代表着，把list中的值，一个个放进lamda的x,y中
l = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x + y, l))

# 如果你给出一个初始值，可以放在list后面
print(reduce(lambda x, y: x + y, l, 10))

'''
    map：
    map函数应用于每一个可迭代的项，返回的是一个结果list
    如果有其他的可迭代参数传进来，map函数则会把每一个参数都以相应的处理函数进行迭代处理
    map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回
    Python函数式编程中的map()函数是将func作用于seq中的每一个元素，并用一个列表给出返回值
    map可以使用任何的lambda函数操作，本质上是把原有的list根据lambda法则变成另外一个list
'''

l = [1, 2, 3]
new_list = list(map(lambda i: i + 1, l))
print(new_list)

# 我们也可以把两个数组搞成一个单独的数组
l2 = [4, 5, 6]
new_list = list(map(lambda x, y: x + y, l, l2))
print(new_list)

'''
    filter：
    filter()函数可以对序列做过滤处理，就是说可以使用一个自定的函数过滤一个序列
    把序列的每一项传到自定义的过滤函数里处理，并返回结果做过滤
    最终一次性返回过滤后的结果
    和map()类似，filter()也接收一个函数和一个序列
    和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
'''

l = [100, 20, 24, 50, 110]
new = list(filter(lambda x: x < 50, l))
print(new)

'''
    装饰器
    用@decorator来装饰某个函数时，其实是做了下面这件事儿：
    -----------------
    @decorator
    def func():
        pass
    变成-------------
    func = decorator(func)
    -----------------
    再简单点说，就是把一个函数传到另外一个函数中，再调回给自己
'''


def hello(fn):
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    print("i am foo")


foo()


def makeHtmlTag(tag, *args, **kwds):
    def real_decorator(fn):
        css_class = " class='{0}'".format(kwds["css_class"]) \
            if "css_class" in kwds else ""

        def wrapped(*args, **kwds):
            return "<" + tag + css_class + ">" + fn(*args, **kwds) + "</" + tag + ">"

        return wrapped

    return real_decorator


@makeHtmlTag(tag="b", css_class="bold_css")
@makeHtmlTag(tag="i", css_class="italic_css")
def hello():
    return "hello world"


print(hello())


class myDecorator(object):
    def __init__(self, fn):
        print("inside myDecorator.__init__()")
        self.fn = fn

    def __call__(self):
        self.fn()
        print("inside myDecorator.__call__()")


@myDecorator
def aFunction():
    print("inside aFunction()")


print("Finished decorating aFunction()")

aFunction()


class makeHtmlTagClass(object):
    def __init__(self, tag, css_class=""):
        self._tag = tag
        self._css_class = " class='{0}'".format(css_class) \
            if css_class != "" else ""

    def __call__(self, fn):
        def wrapped(*args, **kwargs):
            return "<" + self._tag + self._css_class + ">" \
                   + fn(*args, **kwargs) + "</" + self._tag + ">"

        return wrapped


@makeHtmlTagClass(tag="b", css_class="bold_css")
@makeHtmlTagClass(tag="i", css_class="italic_css")
def hello(name):
    return "Hello, {}".format(name)


print(hello("Baby"))


# wraps()消除回调函数名称变更问题，否则会识别函数名为wrapper
def hello(fn):
    @wraps(fn)
    def wrapper():
        print("hello, %s" % fn.__name__)
        fn()
        print("goodby, %s" % fn.__name__)

    return wrapper


@hello
def foo():
    print("i am foo")
    pass


foo()
print(foo.__name__)
print(foo.__doc__)

'''
    *指的是这里可以随便放多少个参数，内部提及的时候，当做一个list看
    **指的也是随便多少个参数，但是这里可以带上参数的名字，比如（x='1', y='2'），内部提及的时候，当做一个dict看
'''

from functools import wraps


def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper


@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(10))

'''
    偏函数：
    Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
    偏函数又可以翻译成部分函数，大概意思就是说，只设置一部分参数
    举个例子，我们知道int()可以把字符串变成十进制数字：
'''
print(int('12345'))

# 8进制转10进制
print(int('12345', base=8))


# 2进制转10进制
def int2(x, base=2):
    return int(x, base)


print(int2("10000000000"))

import functools

int2 = functools.partial(int, base=2)
print(int2('1000000'))

kw = {'base': 2}
print(int('10000000000', **kw))

max2 = functools.partial(max, 10)

print(max2(5, 6, 7))

args = (10, 5, 6, 7)
print(max(*args))
