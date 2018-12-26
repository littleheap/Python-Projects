# -*- coding: utf-8 -*-
# 自定义函数
'''
def functionname( parameters ):
   "函数_文档字符串"
   function_suite
   return [expression]		
'''


def printme(str):
    # "打印传入的字符串到标准显示设备上"
    print(str)
    return


# 函数调用
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


# 可写函数说明
def changeme(mylist):
    # "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


# 参数
def printme(str):
    # "打印任何传入的字符串"
    print(str)

    return


# 调用printme函数
printme()


def printme(str):
    # "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme(str="My string");


def printinfo(name, age):
    # "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki");


def printinfo(name, age=35):
    # "打印任何传入的字符串"
    print("Name: ", name)
    print("Age ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="miki")
printinfo(name="miki")

# 不定长参数
'''
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''


def printinfo(arg1, *vartuple):
    # "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
'''
lambda [arg1 [,arg2,.....argn]]:expression
'''

sum = lambda arg1, arg2: arg1 + arg2;
# 调用sum函数
print("相加后的值为 : ", sum(10, 20))

print("相加后的值为 : ", sum(20, 20))


# return语句
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
total = sum(10, 20)
print("函数外 : ", total)

# 变量的作用范围
total = 0  # 这是一个全局变量


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2  # total在这里是局部变量.
    print("函数内是局部变量 : ", total)
    return total


# 调用sum函数
sum(10, 20)
print("函数外是全局变量 : ", total)

# 键盘输入
str = input("Please enter:");
print("你输入的内容是: ", str)

# 打开与关闭文件
# 打开一个文件
fo = open("foo.txt", "wb")
print("文件名: ", fo.name)

print("是否已关闭 : ", fo.closed)

print("访问模式 : ", fo.mode)

print("末尾是否强制加空格 : ", fo.softspace)

# 打开一个文件
fo = open("foo.txt", "wb")
print("文件名: ", fo.name)

fo.close()

# 打开一个文件
fo = open("foo.txt", "wb")
fo.write("hello\npython");

# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10);
print("读取的字符串是 : ", str)

# 关闭打开的文件
fo.close()

# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取字符串 : ", str)

# 关闭打开的文件
fo.close()

import os

# 重命名文件test1.txt到test2.txt。
os.rename("test1.txt", "test2.txt")

import os

# 删除一个已经存在的文件test2.txt
os.remove("test2.txt")

# 异常处理
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")

else:
    print("Written content in the file successfully")

    fh.close()

try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")

else:
    print("Written content in the file successfully")

try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
finally:
    print("Error: can\'t find file or read data")

try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")

        fh.close()
except IOError:
    print("Error: can\'t find file or read data")

'''
try:
    Business
    Logic
    here...
except "Invalid level!":
    Exception
    handling
    here...
else:
    Rest
    of
    the
    code
    here...
'''


# 自定义异常
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror:
    print()
