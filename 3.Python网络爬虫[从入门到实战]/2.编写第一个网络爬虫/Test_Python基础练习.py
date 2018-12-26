# 循环输出1-100之间的所有奇数

for i in range(100):
    if i % 2 == 1:
        print(i)

# 修改字符串

str1 = '你好$$$我正在学Python@#@#现在需要&%&%&修改字符串'
str2 = str1.replace('$$$', ' ').replace('@#@#', ' ').replace('&%&%&', ' ')
print(str2)  # 你好 我正在学Python 现在需要 修改字符串

# 输出9*9乘法口诀表

for i in range(1, 10):
    for j in range(1, i + 1):
        print("%dx%d=%d\t" % (j, i, i * j), end="")
    print("")
'''
    1x1=1	
    1x2=2	2x2=4	
    1x3=3	2x3=6	3x3=9	
    1x4=4	2x4=8	3x4=12	4x4=16	
    1x5=5	2x5=10	3x5=15	4x5=20	5x5=25	
    1x6=6	2x6=12	3x6=18	4x6=24	5x6=30	6x6=36	
    1x7=7	2x7=14	3x7=21	4x7=28	5x7=35	6x7=42	7x7=49	
    1x8=8	2x8=16	3x8=24	4x8=32	5x8=40	6x8=48	7x8=56	8x8=64	
    1x9=9	2x9=18	3x9=27	4x9=36	5x9=45	6x9=54	7x9=63	8x9=72	9x9=81	
'''


# 按规则求企业的利润奖金

def calcute_profit(I):
    I = I / 10000
    if I <= 10:
        a = I * 0.01
        return a * 10000
    elif I <= 20 and I > 10:
        b = 0.25 + I * 0.075
        return b * 10000
    elif I <= 40 and I > 20:
        c = 0.75 + I * 0.05
        return c * 10000
    elif I <= 60 and I > 40:
        d = 0.95 + I * 0.03
        return d * 10000
    elif I <= 60 and I > 100:
        e = 2 + I * 0.015
        return e * 10000
    else:
        f = 2.95 + I * 0.01
        return f * 10000


# I = int(input('净利润:'))
# profit = calcute_profit(I)
# print('利润为%d元时，应发奖金总数为%d元' % (I, profit))
# '''
#     净利润:210000
#     利润为210000元时，应发奖金总数为18000元
# '''
#
#
# def calcute_profit(I):
#     arr = [1000000, 600000, 400000, 200000, 100000, 0]  # 列表列出分界值
#     rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]  # 列表列出不同分界值对应的奖金比例
#     r = 0  # 总奖金初始值
#     for idx in range(0, 6):  # 6档循环
#         if I > arr[idx]:
#             r = r + (I - arr[idx]) * rat[idx]
#             I = arr[idx]
#     return r
#
#
# I = int(input('净利润:'))
# profit = calcute_profit(I)
# print('利润为%d元时，应发奖金总数为%d元' % (I, profit))
# '''
#     净利润:210000
#     利润为210000元时，应发奖金总数为18000元
# '''

# 字典排序
import operator

x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
print(sorted_x)  # [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]

# 输出判定

a = 1


def fun(a):
    a = 2


fun(a)
print(a)  # 1

a = []


def fun(a):
    a.append(1)


fun(a)
print(a)  # [1]


# 输出判定

class Person:
    name = "aaa"


p1 = Person()
p2 = Person()
p1.name = "bbb"
print(p1.name)  # bbb
print(p2.name)  # aaa
print(Person.name)  # aaa


class Person:
    name = []


p1 = Person()
p2 = Person()
p1.name.append(1)
print(p1.name)  # [1]
print(p2.name)  # [1]
print(Person.name)  # [1]
