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

from numpy.linalg import inv, qr

X = randn(5, 5)
# print(X)
mat = X.T.dot(X)
# print(mat)
# print(inv(mat))  # 逆矩阵
# print(mat.dot(inv(mat)))  # 单位矩阵

q, r = qr(mat)
# print(q)
# print(r)

'''
###随机数生成
samples = np.random.normal(size=(4, 4))
samples

N = 1000000
get_ipython().magic(u'timeit samples = [normalvariate(0, 1) for _ in xrange(N)]')
get_ipython().magic(u'timeit np.random.normal(size=N)')

# 范例：随机漫步
import random

position = 0
walk = [position]
steps = 1000
for i in xrange(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

np.random.seed(12345)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

walk.min()
walk.max()

(np.abs(walk) >= 10).argmax()

# 一次模拟多个随机漫步
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps))  # 0 or 1
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks

walks.max()
walks.min()

hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum()  # 到达30或-30的数量

crossing_times = (np.abs(walks[hits30]) >= 30).argmax(1)
crossing_times.mean()

steps = np.random.normal(loc=0, scale=0.25,
                         size=(nwalks, nsteps))

###利用NumPy进行历史股价分析
import sys

# 读入文件
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

# 计算成交量加权平均价格
vwap = np.average(c, weights=v)
print
"VWAP =", vwap

# 算术平均值函数
print
"mean =", np.mean(c)

# 时间加权平均价格
t = np.arange(len(c))
print
"twap =", np.average(c, weights=t)

# 寻找最大值和最小值
h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)
print
"highest =", np.max(h)
print
"lowest =", np.min(l)
print(np.max(h) + np.min(l)) / 2

print
"Spread high price", np.ptp(h)
print
"Spread low price", np.ptp(l)

# 统计分析

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print
"median =", np.median(c)
sorted = np.msort(c)
print
"sorted =", sorted

N = len(c)
print
"middle =", sorted[(N - 1) / 2]
print
"average middle =", (sorted[N / 2] + sorted[(N - 1) / 2]) / 2

print
"variance =", np.var(c)
print
"variance from definition =", np.mean((c - c.mean()) ** 2)

# 股票收益率
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

returns = np.diff(c) / c[: -1]
print
"Standard deviation =", np.std(returns)

logreturns = np.diff(np.log(c))

posretindices = np.where(returns > 0)
print
"Indices with positive returns", posretindices

annual_volatility = np.std(logreturns) / np.mean(logreturns)
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print
"Annual volatility", annual_volatility

print
"Monthly volatility", annual_volatility * np.sqrt(1. / 12.)

# 日期分析
from datetime import datetime


# Monday 0
# Tuesday 1
# Wednesday 2
# Thursday 3
# Friday 4
# Saturday 5
# Sunday 6
def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()


dates, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 6),
                          converters={1: datestr2num}, unpack=True)
print
"Dates =", dates

averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print
    "Day", i, "prices", prices, "Average", avg
    averages[i] = avg

top = np.max(averages)
print
"Highest average", top
print
"Top day of the week", np.argmax(averages)

bottom = np.min(averages)
print
"Lowest average", bottom
print
"Bottom day of the week", np.argmin(averages)


# 周汇总
def datestr2num(s):
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()


dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',',
                                           usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
close = close[:16]
dates = dates[:16]

# get first Monday
first_monday = np.ravel(np.where(dates == 0))[0]
print
"The first Monday index is", first_monday

# get last Friday
last_friday = np.ravel(np.where(dates == 4))[-1]
print
"The last Friday index is", last_friday

weeks_indices = np.arange(first_monday, last_friday + 1)
print
"Weeks indices initial", weeks_indices

weeks_indices = np.split(weeks_indices, 3)
print
"Weeks indices after split", weeks_indices


def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]

    return ("APPL", monday_open, week_high, week_low, friday_close)


weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print
"Week summary", weeksummary

np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")

# 真实波动幅度均值

h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

N = 20
h = h[-N:]
l = l[-N:]

print
"len(h)", len(h), "len(l)", len(l)
print
"Close", c
previousclose = c[-N - 1: -1]

print
"len(previousclose)", len(previousclose)
print
"Previous close", previousclose
truerange = np.maximum(h - l, h - previousclose, previousclose - l)

print
"True range", truerange

atr = np.zeros(N)

atr[0] = np.mean(truerange)

for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + truerange[i]
    atr[i] /= N

print
"ATR", atr

# 简单移动平均线
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = 5

weights = np.ones(N) / N
print
"Weights", weights

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, sma, lw=2.0)
show()

# 指数移动平均线
x = np.arange(5)
print
"Exp", np.exp(x)
print
"Linspace", np.linspace(-1, 0, 5)

N = 5

weights = np.exp(np.linspace(-1., 0., N))
weights /= weights.sum()
print
"Weights", weights

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, ema, lw=2.0)
show()

# 布林带
N = 5

weights = np.ones(N) / N
print
"Weights", weights

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N - 1:-N + 1]
deviation = []
C = len(c)

for i in range(N - 1, C):
    if i + N < C:
        dev = c[i: i + N]
    else:
        dev = c[-N:]

    averages = np.zeros(N)
    averages.fill(sma[i - N - 1])
    dev = dev - averages
    dev = dev ** 2
    dev = np.sqrt(np.mean(dev))
    deviation.append(dev)

deviation = 2 * np.array(deviation)
print
len(deviation), len(sma)
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N - 1:]
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

print
lowerBB[between_bands]
print
c[between_bands]
print
upperBB[between_bands]
between_bands = len(np.ravel(between_bands))
print
"Ratio between bands", float(between_bands) / len(c_slice)

t = np.arange(N - 1, C)
plot(t, c_slice, lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()

# 线性模型
N = int(sys.argv[1])

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

b = c[-N:]
b = b[::-1]
print
"b", b

A = np.zeros((N, N), float)
print
"Zeros N by N", A

for i in range(N):
    A[i,] = c[-N - 1 - i: - 1 - i]

print
"A", A

(x, residuals, rank, s) = np.linalg.lstsq(A, b)

print
x, residuals, rank, s

print
np.dot(b, x)


# 趋势线
def fit_line(t, y):
    A = np.vstack([t, np.ones_like(t)]).T

    return np.linalg.lstsq(A, y)[0]


h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

pivots = (h + l + c) / 3
print
"Pivots", pivots

t = np.arange(len(c))
sa, sb = fit_line(t, pivots - (h - l))
ra, rb = fit_line(t, pivots + (h - l))

support = sa * t + sb
resistance = ra * t + rb
condition = (c > support) & (c < resistance)
print
"Condition", condition
between_bands = np.where(condition)
print
support[between_bands]
print
c[between_bands]
print
resistance[between_bands]
between_bands = len(np.ravel(between_bands))
print
"Number points between bands", between_bands
print
"Ratio between bands", float(between_bands) / len(c)

print
"Tomorrows support", sa * (t[-1] + 1) + sb
print
"Tomorrows resistance", ra * (t[-1] + 1) + rb

a1 = c[c > support]
a2 = c[c < resistance]
print
"Number of points between bands 2nd approach", len(np.intersect1d(a1, a2))

plot(t, c)
plot(t, support)
plot(t, resistance)
show()
'''
