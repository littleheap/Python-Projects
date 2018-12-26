# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Pandas
# Series：有索引的一维列表
obj = Series([4, 7, -5, 3])
print(obj)

# 数据值
print(obj.values)
# 数据索引
print(obj.index)

# 自定义索引
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
# 数据索引
print(obj2.index)
# 获取数据
print(obj2['a'])

obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

print('b' in obj2)
print('e' in obj2)

# 字典初始化Series
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)

# 列表对齐索引
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)

# 判断非空
print(pd.isnull(obj4))
print(pd.notnull(obj4))

print(obj4.isnull())

# 索引对应运算
print(obj3)
print(obj4)
print(obj3 + obj4)

# 命名key value
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# 重命名索引
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

print('-----------------------------')
print('-----------------------------')

# Dataframe：表格型数据结构，同一列数据类型相同
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)

print(frame)

# 自定义列顺序
print(DataFrame(data, columns=['year', 'state', 'pop']))

# 多余则缺省
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print(frame2)
# 列名
print(frame2.columns)

# 获取列
print(frame2['state'])
print(frame2.year)
# 获取行
print(frame2.ix['three'])

# 赋值列
frame2['debt'] = 16.5
print(frame2)

# 赋值匹配
frame2['debt'] = np.arange(5.)
print(frame2)

# Series赋值
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
print(frame2)

frame2['eastern'] = frame2.state == 'Ohio'
print(frame2)

# 删除列
del frame2['eastern']
print(frame2.columns)

print('-------------------------')
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = DataFrame(pop)
print(frame3)

# 转置行列
print(frame3.T)

# 自定义索引顺序
print(DataFrame(pop, index=[2001, 2002, 2003]))

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
print(DataFrame(pdata))

# 行列索引命名
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)
print(frame3.values)
print(frame2.values)

# 索引对象
obj = Series(range(3), index=['a', 'b', 'c'])
index = obj.index
print(index)

print(index[1:])

# index[1] = 'd'  # 不可直接更改

index = pd.Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index=index)
print(obj2.index is index)

print(frame3)
print('Ohio' in frame3.columns)
print(2003 in frame3.index)
