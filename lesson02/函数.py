# 函数定义和默认参数
def func(x, y=500):
    print(x, y)


func(150)
func(100, 200)
func(y=300, x=100)


# 可变参数
def func(name, *numbers):
    print(name)
    print(numbers)


func('Tom', 1, 2, 3, 4)


# 关键字参数
def func(name, **kvs):
    print(name)
    print(kvs)


func('Jack', china='Beijing', uk='London')


# 命名关键字参数
def func(*, china, uk):  # *用于和普通参数做分割，*args一样效果
    print(china, uk)


func(china='Beijing', uk='London')  # 必须传入参数名


# 复杂情况
def func(a, b, c=0, *args, **kvs):
    print(a, b, c, args, kvs)


func(1, 2)
func(1, 2, 3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', china='Beijing', uk='London')
func(1, 2, 3, *('a', 'b'), **{'china': 'Beijing', 'uk': 'London'})


# 递归的经典例子！
def fib(n):
    if n < 1:
        raise ValueError
    elif (n == 1) or (n == 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
