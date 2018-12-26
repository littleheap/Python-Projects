# -*- coding: utf-8 -*-
# 条件语句
'''
if 判断条件：
    执行语句……
else：
    执行语句……
'''

flag = False
name = 'python'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print('welcome boss')  # 并输出欢迎信息
else:
    print(name)  # 条件不成立时输出变量名称

'''
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
'''

num = 2
if num == 3:  # 判断num的值
    print('boss')

elif num == 2:
    print('user')

elif num == 1:
    print('worker')

elif num < 0:  # 值小于零时输出
    print('error')

else:
    print('roadman')  # 条件均不成立时输出

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print('hello')

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print('hello')

else:
    print('undefine')

num = 8
# 判断值是否在0~5或者10~15之间
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):
    print('hello')

else:
    print('undefine')

var = 100
if (var == 100): print("变量 var 的值为100")

print("Good bye!")

# while语句
'''
while 判断条件：
    执行语句……
'''
count = 0
while (count < 9):
    print('The count is:', count)

    count = count + 1

print("Good bye!")

# continue 和 break 用法

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print(i)  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print(i)  # 输出1~10

    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

# 死循环
'''
var = 1
while var == 1 :  # 该条件永远为true，循环将无限执行下去
   num = raw_input("Enter a number  :")
   print "You entered: ", num

print "Good bye!"
'''

# while … else
count = 0
while count < 5:
    print(count, " is  less than 5")

    count = count + 1
else:
    print(count, " is not less than 5")

# 简单语句组
flag = 0
while (flag): print('Given flag is really true!')

flag = 0
print("Good bye!")

# for语句
'''
for iterating_var in sequence:
   statements(s)
'''
for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

print("Good bye!")

# 序列索引迭代
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print('当前水果 :', fruits[index])

print("Good bye!")

# for...else
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print(num, '是一个质数')

# 嵌套循环
i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")

# break语句
for letter in 'Python':  # First Example
    if letter == 'h':
        break
    print('Current Letter :', letter)

var = 10  # Second Example
while var > 0:
    print('Current variable value :', var)

    var = var - 1
    if var == 5:
        break

print("Good bye!")

# continue语句
for letter in 'Python':  # 第一个实例
    if letter == 'h':
        continue
    print('当前字母 :', letter)

var = 10  # 第二个实例
while var > 0:
    var = var - 1
    if var == 5:
        continue
    print('当前变量值 :', var)

print("Good bye!")

# pass语句
# 输出 Python 的每个字母
for letter in 'Python':
    if letter == 'h':
        pass
        print('这是 pass 块')
    print('当前字母 :', letter)

print("Good bye!")

# 格式字符串
print("My name is %s and weight is %d kg!" % ('Zara', 21))

# 时间与日期
import time  # This is required to include time module.

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

localtime = time.localtime(time.time())
print("Local current time :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

import calendar

cal = calendar.month(2008, 1)
print("Here is the calendar:")

print(cal)
