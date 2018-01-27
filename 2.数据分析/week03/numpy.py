# -*- coding: utf-8 -*-
# 向量相加-Python
def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    for i in range(len(a)):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b[i])
    return c


# print(pythonsum(3))

# 向量相加-NumPy


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c


# print(numpysum(3))

# 效率比较
from datetime import datetime

import numpy as np

size = 1000

start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
# print("The last 2 elements of the sum", c[-2:])
# print("PythonSum elapsed time in microseconds", delta.microseconds)

start = datetime.now()
c = numpysum(size)
delta = datetime.now() - start
# print("The last 2 elements of the sum", c[-2:])
# print("NumPySum elapsed time in microseconds", delta.microseconds)


# numpy数组
a = np.arange(5)
# print(a.dtype)
# print(a)
# print(a.shape)

# 创建多维数组
m = np.array([np.arange(2), np.arange(2)])
# print(m)
# print(m.shape)
# print(m.dtype)
# print(np.zeros(10))
# print(np.zeros((3, 6)))
# print(np.empty((2, 3, 2)))
# print(np.arange(15))


# 选取数组元素
a = np.array([[1, 2], [3, 4]])

# print("In: a")
# print(a)
#
# print("In: a[0,0]")
# print(a[0, 0])
# print("In: a[0,1]")
# print(a[0, 1])
#
# print("In: a[1,0]")
# print(a[1, 0])
#
# print("In: a[1,1]")
# print(a[1, 1])

# numpy数据类型
# print("In: float64(42)")
# print(np.float64(42))
#
# print("In: int8(42.0)")
# print(np.int8(42.0))
#
# print("In: bool(42)")
# print(np.bool(42))
#
# print(np.bool(0))
#
# print("In: bool(42.0)")
# print(np.bool(42.0))
#
# print("In: float(True)")
# print(np.float(True))
# print(np.float(False))
#
# print("In: arange(7, dtype=uint16)")
# print(np.arange(7, dtype=np.uint16))
#
# print("In: int(42.0 + 1.j)")
#
# #Type error
# try:
#     print(np.int(42.0 + 1.j))
# except TypeError:
#     print("TypeError")

# Type error
# print("In: float(42.0 + 1.j)")
# print(float(42.0 + 1.j))


# 数据类型转换
arr = np.array([1, 2, 3, 4, 5])
# print(arr.dtype)
float_arr = arr.astype(np.float64)
# print(float_arr.dtype)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
# print(arr)
# print(arr.astype(np.int32))

numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
# print(numeric_strings.astype(float))


# 数据类型对象
a = np.array([[1, 2], [3, 4]])

# print(a.dtype.byteorder)
#
# print(a.dtype.itemsize)

# 字符编码
# print(np.arange(7, dtype='f'))
# print(np.arange(7, dtype='D'))
#
# print(np.dtype(float))
#
# print(np.dtype('f'))
#
# print(np.dtype('d'))
#
# print(np.dtype('f8'))
#
# print(np.dtype('Float64'))

# dtype类的属性
t = np.dtype('Float64')
# print(t.char)
# print(t.type)
# print(t.str)


# 创建自定义数据类型
t = np.dtype([('name', np.str_, 40), ('numitems', np.int32), ('price', np.float32)])
# print(t)
# print(t['name'])
itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
# print(itemz[1])

# 数组与标量的运算
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(arr)
# print(arr * arr)
# print(arr - arr)
# print(1 / arr)
# print(arr ** 0.5)


# 一维数组的索引与切片
a = np.arange(9)
# print(a[3:7])
# 0到7步长为2
# print(a[:7:2])
# 倒序
# print(a[::-1])

# 同a[3:7:2]
s = slice(3, 7, 2)
# print(a[s])
# 同a[0:0:-1]
s = slice(None, None, -1)
# print(a[s])

# 多维数组的切片与索引
# 实际上：3*4*2
b = np.arange(24).reshape(2, 3, 4)

# print(b.shape)
# print("------------------")
# print(b)
# print("------------------")
# print(b[0, 0, 0])
# print("------------------")
# print(b[:, 0, 0])
# print("------------------")
# print(b[0])
# print("------------------")
# print(b[0, :, :])
# print("------------------")
# print(b[0, ...])
# print("------------------")
# print(b[0, 1])
# print("------------------")
# print(b[0, 1, ::2])
# print("------------------")
# print(b[..., 1])
# print("------------------")
# print(b[:, 1])
# print("------------------")
# print(b[0, :, 1])
# print("------------------")
# print(b[0, :, -1])
# print("------------------")
# print(b[0, ::-1, -1])
# print("------------------")
# print(b[0, ::2, -1])
# print("------------------")
# print(b[::-1])
# print("------------------")

s = slice(None, None, -1)
# print(b[(s, s, s)])

# 布尔型索引

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
# print(names)
# print(data)

# print(names == 'Bob')
# print(data[names == 'Bob'])

# print(data[names == 'Bob', 2:])
# print(data[names == 'Bob', 3])

names != 'Bob'
# print(data[-(names == 'Bob')])

mask = (names == 'Bob') | (names == 'Will')
# print(mask)
# print(data[mask])

data[data < 0] = 0
# print(data)

data[names != 'Joe'] = 7
# print(data)

# 花式索引
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i
# print(arr)

# print(arr[[4, 3, 0, 6]])
# print(arr[[-3, -5, -7]])

arr = np.arange(32).reshape((8, 4))
# print(arr)
# 获取4个（m,n）
# print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
# 单排重排序
# print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
# 同上
# print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])

# 数组转置
arr = np.arange(15).reshape((3, 5))
# print(arr)
# print(arr.T)

# 改变数组的维度
b = np.arange(24).reshape(2, 3, 4)
# print(b)
# print(b.ravel())
# print(b.flatten())

b.shape = (6, 4)
# print(b)
# print(b.transpose())

b.resize((2, 12))
# print(b)

# 组合数组
a = np.arange(9).reshape(3, 3)
# print(a)

b = 2 * a
# print(b)
# 水平组合
# print(np.hstack((a, b)))
# 水平组合
# print(np.concatenate((a, b), axis=1))
# 垂直组合
# print(np.vstack((a, b)))
# 垂直组合
# print(np.concatenate((a, b), axis=0))
# 深度组合
# print(np.dstack((a, b)))

oned = np.arange(2)
# print(oned)
twice_oned = 2 * oned
# print(twice_oned)
'''
# 列组合
print(np.column_stack((oned, twice_oned)))
# 列组合即水平组合
print(np.column_stack((a, b)))
# 两种方法一样
print(np.column_stack((a, b)) == np.hstack((a, b)))
# 行组合
print(np.row_stack((oned, twice_oned)))
# 行组合即垂直组合
print(np.row_stack((a, b)))
# 两种方法完全一样
print(np.row_stack((a, b)) == np.vstack((a, b)))
'''

# 数组的分割
a = np.arange(9).reshape(3, 3)
'''
print(a)
# 纵向分割
print(np.hsplit(a, 3))
# 纵向分割
print(np.split(a, 3, axis=1))
# 水平分割
print(np.vsplit(a, 3))
# 水平分割
print(np.split(a, 3, axis=0))
'''

c = np.arange(27).reshape(3, 3, 3)
# 深度分割
# print(c)
# print(np.dsplit(c, 3))


# 数组的属性
b = np.arange(24).reshape(2, 12)
'''
# 维度
print(b.ndim)
# 尺寸（个数）
print(b.size)
# 每个元素的字节数
print(b.itemsize)
# 内存大小，上面的乘积
print(b.nbytes)
'''

# 虚数
b = np.array([1. + 1.j, 3. + 2.j])
# print(b.real)
# print(b.imag)

b = np.arange(4).reshape(2, 2)
# 类型
# print(b.flat)
# 展开成以为数组，用索引获取，还可以赋值
# print(b.flat[2])

# 数组的转换
b = np.array([1. + 1.j, 3. + 2.j])
# print(b)
# 转换成列表
# print(b.tolist())
# 转换成字符串
# print(b.tostring())

# print(np.fromstring('20:42:52', sep=':', dtype=int))

# print(b)
# 虚数转实数，有数据丢失风险，因为丢掉了虚部
# print(b.astype(int))
# 实数转虚数
# print(b.astype('complex'))
