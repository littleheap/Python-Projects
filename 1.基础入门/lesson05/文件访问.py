file1 = open("./files/test.txt")
file2 = open("./files/output.txt", "w")

while True:
    line = file1.readline()
    # 这里可以进行逻辑处理
    file2.write(line)
    if not line:
        break
        # 记住文件处理完，关闭是个好习惯
file1.close()
file2.close()

'''
读文件有3种方法：
    read()将文本文件所有行读到一个字符串中。
    readline()是一行一行的读
    readlines()是将文本文件中所有行读到一个list中，文本文件每一行是list的一个元素。 
    优点：readline()可以在读行过程中跳过特定行。

'''

file2 = open("./files/output.txt", "w")
for line in open("./files/test.txt"):
    # 这里可以进行逻辑处理
    file2.write(line)

# 打开文件
# 用with...open自带关闭文本的功能
with open('./files/somefile.txt', 'r') as f:
    data = f.read()

# loop整个文档
with open('./files/somefile.txt', 'r') as f:
    for line in f:
        # 处理每一行
        pass

# 写入文本
with open('./files/somefile.txt', 'w') as f:
    f.write("A")
    f.write("B")
    ...

# 把要打印的line写入文件中
with open('./files/somefile.txt', 'w') as f:
    print("A", file=f)
    print("B", file=f)

# Python默认读取的都是文本文件。要是想要读取二进制文件，需要把刚刚的'r'改成'rb'.

f = open('./files/photo.JPG', 'rb')
print(f.read())
# 输出十六进制表示的字节

# f = open('./files/DegangGuo.txt', 'rb')
# 读入作文, 但是参合着错别字的繁体编码，假设叫个"DeyunCode"
# 读入以后，就需要解码
# u = f.read().decode('DeyunCode')

import os

# 当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
print(os.path.join('./files/', 'Pictures'))
# 这里你得到的是一个字符串，代表了新的文件夹是这个位置：/Users/EDC/Pictures/

# 需要用mkdir创建：
os.mkdir('./files/Pictures/')

# 同理，删除一个文件夹
os.rmdir('./files/Pictures/')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('./files/Pictures/movie.avi'))

# 或者靠os.path.splitext()得到文件扩展名：
print(os.path.splitext('./files/Pictures/movie.avi'))

# 文件重命名
# os.rename('test.txt', 'newtest.txt')

# 删除文件
# os.remove('newtest.txt')

# 复制文件
# shutil.copyfile('./other.txt', './files/other.txt')

# 列出当前目录下的所有文件夹：
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 只想列出.py文件：
print([x for x in os.listdir('../lesson01') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
