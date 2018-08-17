def hello(who='world'):
    print('hello %s!' % (who))


hello()  # hello world!
hello('sea')  # hello sea!


# f(x) = x * 5 + 100
# g(x) = x * 5; f(x) = x + 100
# => f(g(x)) = x * 5 + 100
def g(x):
    return x * 5


def f(gf, x):
    return gf(x) + 100


print(f(g, 100))  # 600

print(f(lambda x: x * 5, 100))  # 600


def f(gf, x, y):
    return gf(x, y) + 100


print(f(lambda x, y: x * y, 100, 200))  # 20100
