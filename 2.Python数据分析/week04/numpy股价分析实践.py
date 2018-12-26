# 利用NumPy进行历史股价分析
import numpy as np

# 读入文件，获取第7和8列字段（收盘价 || 成交量）
c, v = np.loadtxt('data.csv', delimiter=',', usecols=(6, 7), unpack=True)

# 计算成交量加权平均价格
vwap = np.average(c, weights=v)
print("VWAP =", vwap)

# 算术平均值函数
print("mean =", np.mean(c))

# 时间加权平均价格，时间近权重大
t = np.arange(len(c))
print("twap =", np.average(c, weights=t))

# 寻找最大值和最小值
h, l = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5), unpack=True)
print("highest =", np.max(h))
print("lowest =", np.min(l))

# 最高价最低价平均值
print((np.max(h) + np.min(l)) / 2)

# 最高价取值范围
print("Spread high price", np.ptp(h))
# 最低价取值范围
print("Spread low price", np.ptp(l))

# 统计分析
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
# 中位数
print("median =", np.median(c))

# 排序
sorted = np.msort(c)
print("sorted =", sorted)

# 方差
N = len(c)
print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean()) ** 2))

# 股票收益率
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

# 差分，相邻差值
returns = np.diff(c) / c[: -1]
print("Standard deviation =", np.std(returns))

# 对数收益率
logreturns = np.diff(np.log(c))
posretindices = np.where(returns > 0)  # 收益率大于0
print("Indices with positive returns", posretindices)

# 年化波动率
# 对数收益率标准差/均值
annual_volatility = np.std(logreturns) / np.mean(logreturns)
# 再/交易日倒数的平方
annual_volatility = annual_volatility / np.sqrt(1. / 252.)
print("Annual volatility", annual_volatility)

# 月度波动率
print("Monthly volatility", annual_volatility * np.sqrt(1. / 12.))

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
    return datetime.strptime(s.decode('ascii'), "%d-%m-%Y").date().weekday()


# 读取日期 || 收盘价
dates, close = np.loadtxt('data.csv', delimiter=',', usecols=(1, 6),
                          converters={1: datestr2num}, unpack=True)
print("Dates =", dates)

# 5个工作日数组
averages = np.zeros(5)

for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close, indices)
    avg = np.mean(prices)
    print("Day", i, "prices", prices, "Average", avg)
    averages[i] = avg

top = np.max(averages)
print("Highest average", top)
print("Top day of the week", np.argmax(averages))

bottom = np.min(averages)
print("Lowest average", bottom)
print("Bottom day of the week", np.argmin(averages))


# 周汇总
def datestr2num(s):
    return datetime.strptime(s.decode('ascii'), "%d-%m-%Y").date().weekday()


# 读取日期 || 开盘价 || 最高价 || 最低价 || 收盘价
dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',',
                                           usecols=(1, 3, 4, 5, 6), converters={1: datestr2num}, unpack=True)
# 前三周数据
close = close[:16]
dates = dates[:16]

# 获取第一个星期一的索引
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is", first_monday)

# 获取最后一个星期五的索引
last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is", last_friday)

# 重新编排索引
weeks_indices = np.arange(first_monday, last_friday + 1)
print("Weeks indices initial", weeks_indices)

# 三周分成三组
weeks_indices = np.split(weeks_indices, 3)
print("Weeks indices after split", weeks_indices)


# 周汇总
def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l, a))
    friday_close = c[a[-1]]

    return ("APPL", monday_open, week_high, week_low, friday_close)


weeksummary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print("Week summary", weeksummary)

# 保存到CSV文件
np.savetxt("weeksummary.csv", weeksummary, delimiter=",", fmt="%s")

# ATR真实波动幅度均值
# 获取最高价 || 最低价 || 收盘价
h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

# 获取最后20个数据
N = 20
h = h[-N:]
l = l[-N:]

print("len(h)", len(h), "len(l)", len(l))
print("Close", c)

# 最后20个数据的对应的前一天数据
previousclose = c[-N - 1: -1]

print("len(previousclose)", len(previousclose))
print("Previous close", previousclose)

# 三种数据差值
truerange = np.maximum(h - l, h - previousclose, previousclose - l)
print("True range", truerange)

# 20天空间数组
atr = np.zeros(N)

# 真实率浮动平均值
atr[0] = np.mean(truerange)

# 公式计算ATR
for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + truerange[i]
    atr[i] /= N

print("ATR", atr)

# 简单移动平均线
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 滑动窗口
N = 5

weights = np.ones(N) / N
print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
# 简单移动平均值SMA
sma = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, sma, lw=2.0)
show()

# 指数移动平均线
x = np.arange(5)
print("Exp", np.exp(x))
print("Linspace", np.linspace(-1, 0, 5))

N = 5
weights = np.exp(np.linspace(-1., 0., N))
weights /= weights.sum()
print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights, c)[N - 1:-N + 1]
t = np.arange(N - 1, len(c))
plot(t, c[N - 1:], lw=1.0)
plot(t, ema, lw=2.0)
show()

# 布林带
N = 5

weights = np.ones(N) / N
print("Weights", weights)

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
print(len(deviation), len(sma))

# 上限
upperBB = sma + deviation
# 下限
lowerBB = sma - deviation

c_slice = c[N - 1:]
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))

print(lowerBB[between_bands])

print(c[between_bands])

print(upperBB[between_bands])

between_bands = len(np.ravel(between_bands))
print("Ratio between bands", float(between_bands) / len(c_slice))

t = np.arange(N - 1, C)
plot(t, c_slice, lw=1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()

# 线性模型
N = 5

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

b = c[-N:]
b = b[::-1]
print("b", b)

A = np.zeros((N, N), float)
print("Zeros N by N", A)

for i in range(N):
    A[i,] = c[-N - 1 - i: - 1 - i]

print("A", A)

(x, residuals, rank, s) = np.linalg.lstsq(A, b)

print(x, residuals, rank, s)

print(np.dot(b, x))


# 趋势线
def fit_line(t, y):
    A = np.vstack([t, np.ones_like(t)]).T

    return np.linalg.lstsq(A, y)[0]


h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

pivots = (h + l + c) / 3
print("Pivots", pivots)

t = np.arange(len(c))
sa, sb = fit_line(t, pivots - (h - l))
ra, rb = fit_line(t, pivots + (h - l))

support = sa * t + sb
resistance = ra * t + rb
condition = (c > support) & (c < resistance)
print("Condition", condition)

between_bands = np.where(condition)
print(support[between_bands])

print(c[between_bands])

print(resistance[between_bands])

between_bands = len(np.ravel(between_bands))
print("Number points between bands", between_bands)

print("Ratio between bands", float(between_bands) / len(c))

print("Tomorrows support", sa * (t[-1] + 1) + sb)

print("Tomorrows resistance", ra * (t[-1] + 1) + rb)

a1 = c[c > support]
a2 = c[c < resistance]
print("Number of points between bands 2nd approach", len(np.intersect1d(a1, a2)))

plot(t, c)
plot(t, support)
plot(t, resistance)
show()
