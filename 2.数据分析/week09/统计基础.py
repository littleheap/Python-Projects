# -*- coding: utf-8 -*-

import pandas as pd
from pandas import Series, DataFrame
import numpy as np

a = [98, 83, 65, 72, 79, 76, 75, 94, 91, 77, 63, 83, 89, 69, 64, 78, 63, 86, 91, 72, 71, 72, 70, 80, 65, 70, 62, 74, 71,
     76]

print(np.mean(a))

print(np.mean(np.sort(a)[14:16]))

print(np.sort(a))


# 求众数的函数
def get_mode(arr):
    mode = []
    arr_appear = dict((a, arr.count(a)) for a in arr)  # 统计各个元素出现的次数
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1  
        return  # 则没有众数
    else:
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(arr_appear.values()):
                mode.append(k)
    return mode


print(get_mode(a))

print(np.var(a))

print(np.std(a))

a = Series(a)

print(a.skew())

print(a.kurt())

print(a.describe())

df = DataFrame({'data1': np.random.randn(5),
                'data2': np.random.randn(5)})
print(df.cov())

print(df.corr())

# 假设检验
from scipy import stats as ss

df = DataFrame({'data': [10.1, 10, 9.8, 10.5, 9.7, 10.1, 9.9, 10.2, 10.3, 9.9]})

print(ss.ttest_1samp(a=df, popmean=10))
