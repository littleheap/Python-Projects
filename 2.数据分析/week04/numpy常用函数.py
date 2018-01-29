# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
from numpy.random import randn

# 通用函数
arr = np.arange(10)
# print(arr)
# print(np.sqrt(arr))
# print(np.exp(arr))

x = randn(8)
y = randn(8)
# print(x)
# print(y)
# print(np.maximum(x, y))  # 元素级最大值

arr = randn(7)
# print(arr)
# print(np.modf(arr))  # 分解整数小数部分

# 利用数组进行数据处理
# 向量化
points = np.arange(-5, 5, 0.01)  # 1000均等分点
xs, ys = np.meshgrid(points, points)
# print(xs)
# print(ys)

z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)
# plt.imshow(z, cmap=plt.cm.gray);
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
# plt.draw()
# plt.show()

# 将条件逻辑表达为数组运算
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y)
          for x, y, c in zip(xarr, yarr, cond)]
# print(result)

result = np.where(cond, xarr, yarr)
# print(result)

arr = randn(4, 4)
# print(arr)
# print(np.where(arr > 0, 2, -2))  # 大于0为2，小于0为-2
# print(np.where(arr > 0, 2, arr))  # 大于0为2

'''
result = []
for i in range(n):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)

# Not to be executed
np.where(cond1 & cond2, 0,
         np.where(cond1, 1,
                  np.where(cond2, 2, 3)))

# Not to be executed
result = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)
'''

# 数学与统计方法
arr = np.random.randn(5, 4)  # 标准正态分布数据
# print(arr)
# print(arr.mean())
# print(np.mean(arr))
# print(arr.sum())

# print(arr.mean(axis=1))  # 每一行均值
# print(arr.sum(0))  # 每一列和

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# print(arr)
# print(arr.cumsum(0))  # 累计和
# print(arr.cumprod(1))  # 累计积

# 用于布尔型数组的方法
arr = randn(100)
# print(arr)
# print((arr > 0).sum())  # 正值的数量

bools = np.array([False, False, True, False])
# print(bools.any())  # 是否有一个true
# print(bools.all())  # 是否全部为true

# 排序
arr = randn(8)
# print(arr)
arr.sort()
# print(arr)

arr = randn(5, 3)
# print(arr)
arr.sort(1)  # 按行维度排序
# print(arr)

large_arr = randn(1000)
# print(large_arr)
large_arr.sort()  # 先排序
# print(large_arr[int(0.05 * len(large_arr))])  # 5%分位数

# 唯一化以及其他的集合逻辑
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# print(np.unique(names))
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
# print(np.unique(ints))
# print(sorted(set(names)))

# 元素是否在已有数组中
values = np.array([6, 0, 0, 3, 2, 5, 6])
# print(np.in1d(values, [2, 3, 6]))

# 线性代数
x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
# print(x)
# print(y)
# print(x.dot(y))  # 等价于np.dot(x, y)矩阵乘法
# print(np.dot(x, np.ones(3)))

# print(np.random.seed(12345))

from numpy.linalg import qr

X = randn(5, 5)
# print(X)
mat = X.T.dot(X)
# print(mat)
# print(inv(mat))  # 逆矩阵
# print(mat.dot(inv(mat)))  # 单位矩阵

q, r = qr(mat)
# print(q)
# print(r)

# 随机数生成
samples = np.random.normal(size=(4, 4))
# print(samples)

N = 1000000
# print(get_ipython().magic(u'timeit samples = [normalvariate(0, 1) for _ in xrange(N)]'))
# print(get_ipython().magic(u'timeit np.random.normal(size=N)'))

'''
# 范例：随机漫步
import random

position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)
# print(walk)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())
print((np.abs(walk) >= 10).argmax())
'''

'''
# 一次模拟多个随机漫步
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
print(walks)

print(walks.max())
print(walks.min())

hits30 = (np.abs(walks) >= 30).any(1)
print(hits30)
print(hits30.sum())  # 到达30或-30的数量

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
print(crossing_times.mean())

steps = np.random.normal(loc=0, scale=0.25,
                         size=(nwalks, nsteps))
'''
