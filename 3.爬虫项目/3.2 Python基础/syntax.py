a = 1234
print(a)  # 1234
a = 'abcd'
print(a)  # abcd

try:
    print(a)  # abcd
except Exception as e:
    print(e)

a = [1, 2, 3, 4]


def func(a):
    a[0] = 2


func(a)
print(a)  # [2, 2, 3, 4]
