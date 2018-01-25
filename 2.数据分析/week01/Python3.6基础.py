# -*- coding: utf-8 -*-

print("Hello, Python!");

# 行和缩进
if True:
    print("True")
else:
    print("False")

if True:
    print("Answer")
    print("True")

else:
    print("Answer")
    # 没有严格缩进，在执行时保持
    print("False")

# 多行语句
item_one = 1
item_two = 2
item_three = 3
total = item_one + \
        item_two + \
        item_three
print(total)

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
print(days)

# 引号
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
print(word)

print(sentence)

print(paragraph)

# 注释
# 第一个注释
print("Hello, Python!")
# 第二个注释
name = "Madisetti"  # 这是一个注释

'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''

"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""

# 空行
str = input("\n\nPress the enter key to exit.")

import sys

x = 'foo'
sys.stdout.write(x + '\n')

# 码组
'''
if expression : 
   suite 
elif expression :  
   suite  
else :  
   suite 
'''

# 帮助
help(sys.stdout.write)

# 变量赋值
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print(counter)

print(miles)

print(name)

a = b = c = 1
print(a, b, c)

a, b, c = 1, 2, "john"
print(a, b, c)

# 数字
var1 = 1
var2 = 10

# del var1[,var2[,var3[....,varN]]]]
var = 5896419821
var_a = 0.22
var_b = 3e2
del var
del var_a, var_b

# 字符串
# s="a1a2•••an"(n>=0)

s = 'ilovepython'
print(s[1:5])

print(s[5:-1])

str = 'Hello World!'
print(str)  # 输出完整字符串

print(str[0])  # 输出字符串中的第一个字符

print(str[2:5])  # 输出字符串中第三个至第五个之间的字符串

print(str[2:])  # 输出从第三个字符开始的字符串

print(str * 2)  # 输出字符串两次

print(str + "TEST")  # 输出连接的字符串

# 列表
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # 输出完整列表

print(list[0])  # 输出列表的第一个元素

print(list[1:3])  # 输出第二个至第三个的元素

print(list[2:])  # 输出从第三个开始至列表末尾的所有元素

print(tinylist * 2)  # 输出列表两次

print(list + tinylist)  # 打印组合的列表

# 元组
tuple = ('abcd', 786, 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(tuple)  # 输出完整元组

print(tuple[0])  # 输出元组的第一个元素

print(tuple[1:3])  # 输出第二个至第三个的元素

print(tuple[2:])  # 输出从第三个开始至列表末尾的所有元素

print(tinytuple * 2)  # 输出元组两次

print(tuple + tinytuple)  # 打印组合的元组

tuple = ('abcd', 786, 2.23, 'john', 70.2)
list = ['abcd', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000  # 元组中是非法应用
list[2] = 1000  # 列表中是合法应用

# 元字典
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # 输出键为'one' 的值

print(dict[2])  # 输出键为 2 的值

print(tinydict)  # 输出完整的字典

print(tinydict.keys())  # 输出所有键

print(tinydict.values())  # 输出所有值

# 算术运算符
a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c = a - b
print("Line 2 - Value of c is ", c)

c = a * b
print("Line 3 - Value of c is ", c)

c = a / b
print("Line 4 - Value of c is ", c)

c = a % b
print("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a ** b
print("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a // b
print("Line 7 - Value of c is ", c)

# 比较运算符
a = 21
b = 10
c = 0

if (a == b):
    print("Line 1 - a is equal to b")

else:
    print("Line 1 - a is not equal to b")

if (a != b):
    print("Line 2 - a is not equal to b")

else:
    print
    "Line 2 - a is equal to b"

if (a != b):
    print("Line 3 - a is not equal to b")

else:
    print("Line 3 - a is equal to b")

if (a < b):
    print("Line 4 - a is less than b")

else:
    print("Line 4 - a is not less than b")

if (a > b):
    print("Line 5 - a is greater than b")

else:
    print("Line 5 - a is not greater than b")

a = 5
b = 20
if (a <= b):
    print("Line 6 - a is either less than or equal to  b")

else:
    print("Line 6 - a is neither less than nor equal to  b")

if (b >= a):
    print("Line 7 - b is either greater than  or equal to b")

else:
    print("Line 7 - b is neither greater than  nor equal to b")

# 赋值运算符
a = 21
b = 10
c = 0

c = a + b
print("Line 1 - Value of c is ", c)

c += a
print("Line 2 - Value of c is ", c)

c *= a
print("Line 3 - Value of c is ", c)

c /= a
print("Line 4 - Value of c is ", c)

c = 2
c %= a
print("Line 5 - Value of c is ", c)

c **= a
print("Line 6 - Value of c is ", c)

c //= a
print("Line 7 - Value of c is ", c)

# 位运算符
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("Line 1 - Value of c is ", c)

c = a | b  # 61 = 0011 1101
print("Line 2 - Value of c is ", c)

c = a ^ b  # 49 = 0011 0001
print("Line 3 - Value of c is ", c)

c = ~a  # -61 = 1100 0011
print("Line 4 - Value of c is ", c)

c = a << 2  # 240 = 1111 0000
print("Line 5 - Value of c is ", c)

c = a >> 2  # 15 = 0000 1111
print("Line 6 - Value of c is ", c)

# 逻辑运算符
a = 10
b = 20
c = 0

if (a and b):
    print("Line 1 - a and b are true")

else:
    print("Line 1 - Either a is not true or b is not true")

if (a or b):
    print("Line 2 - Either a is true or b is true or both are true")

else:
    print("Line 2 - Neither a is true nor b is true")

a = 0
if (a and b):
    print("Line 3 - a and b are true")

else:
    print("Line 3 - Either a is not true or b is not true")

if (a or b):
    print("Line 4 - Either a is true or b is true or both are true")

else:
    print("Line 4 - Neither a is true nor b is true")

if not (a and b):
    print("Line 5 - Either a is not true or b is  not true or both are not true")
else:
    print("Line 5 - a and b are true")

# 成员运算符
a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print("Line 1 - a is available in the given list")

else:
    print("Line 1 - a is not available in the given list")

if (b not in list):
    print("Line 2 - b is not available in the given list")

else:
    print("Line 2 - b is available in the given list")

a = 2
if (a in list):
    print("Line 3 - a is available in the given list")

else:
    print("Line 3 - a is not available in the given list")

# 身份运算符
a = 20
b = 20

if (a is b):
    print("Line 1 - a and b have same identity")

else:
    print("Line 1 - a and b do not have same identity")

if (id(a) == id(b)):
    print("Line 2 - a and b have same identity")

else:
    print("Line 2 - a and b do not have same identity")

b = 30
if (a is b):
    print("Line 3 - a and b have same identity")

else:
    print("Line 3 - a and b do not have same identity")

if (a is not b):
    print("Line 4 - a and b do not have same identity")

else:
    print("Line 4 - a and b have same identity")

# 运算符优先级
a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("Value of (a + b) * c / d is ", e)

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("Value of ((a + b) * c) / d is ", e)

e = (a + b) * (c / d)  # (30) * (15/5)
print("Value of (a + b) * (c / d) is ", e)

e = a + (b * c) / d  # 20 + (150/5)
print("Value of a + (b * c) / d is ", e)
