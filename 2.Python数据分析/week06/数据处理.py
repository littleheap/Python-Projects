from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数

np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd

np.set_printoptions(precision=4, threshold=500)
pd.options.display.max_rows = 100

# 缺失值处理——拉格朗日插值法
inputfile = './data/catering_sale.xls'  # 销量数据路径
outputfile = './data/sales.xls'  # 输出数据路径

data = pd.read_excel(inputfile)  # 读入数据
print(data)
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None  # 过滤异常值，将其变为空值
print(data)


# 自定义列向量插值函数
# s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


# 逐个元素判断是否需要插值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:  # 如果为空即插值。
            data[i][j] = ployinterp_column(data[i], j)

print(data)
data.to_excel(outputfile)  # 输出结果，写入文件

print('-------------------------')
# dataframe合并
# 1
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df2 = DataFrame({'key': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df1)
print(df2)

df = pd.merge(df1, df2)
print(df)
df = pd.merge(df1, df2, on='key')  # 指定键
print(df)

# 2
df3 = DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                 'data1': range(7)})
df4 = DataFrame({'rkey': ['a', 'b', 'd'],
                 'data2': range(3)})
print(df3)
print(df4)

df = pd.merge(df3, df4, left_on='lkey', right_on='rkey')
print(df)

df = pd.merge(df1, df2, how='outer')  # 外连接：并集
print(df)

# 3
df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                 'data1': range(6)})
df2 = DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                 'data2': range(5)})
print(df1)
print(df2)

df = pd.merge(df1, df2, on='key', how='left')  # 左连接：以df1键为目标，df1提供键
print(df)

df = pd.merge(df1, df2, how='inner')  # 内连接：交集
print(df)

# 4
left = DataFrame({'key1': ['foo', 'foo', 'bar'],
                  'key2': ['one', 'two', 'one'],
                  'lval': [1, 2, 3]})
right = DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                   'key2': ['one', 'one', 'one', 'two'],
                   'rval': [4, 5, 6, 7]})
print(left)
print(right)

df = pd.merge(left, right, on=['key1', 'key2'], how='outer')  # 多键连接
print(df)

# 5
df = pd.merge(left, right, on='key1')
print(df)

df = pd.merge(left, right, on='key1', suffixes=('_left', '_right'))  # 自定义复键子名称
print(df)

print('-------------------------')
# 索引上的合并
# 1
left1 = DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'], 'value': range(6)})
right1 = DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])
print(left1)
print(right1)

df = pd.merge(left1, right1, left_on='key', right_index=True)
print(df)

df = pd.merge(left1, right1, left_on='key', right_index=True, how='outer')
print(df)

# 2
lefth = DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                   'key2': [2000, 2001, 2002, 2001, 2002],
                   'data': np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                   index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                          [2001, 2000, 2000, 2000, 2001, 2002]],
                   columns=['event1', 'event2'])
print(lefth)
print(righth)

df = pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)
print(df)

df = pd.merge(lefth, righth, left_on=['key1', 'key2'],
              right_index=True, how='outer')
print(df)

left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]], index=['a', 'c', 'e'],
                  columns=['Ohio', 'Nevada'])
right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                   index=['b', 'c', 'd', 'e'], columns=['Missouri', 'Alabama'])
print(left2)
print(right2)
df = pd.merge(left2, right2, how='outer', left_index=True, right_index=True)
print(df)

# 3
print(left2)
print(right2)
df = left2.join(right2, how='outer')
print(df)

print(left1)
print(right1)
df = left1.join(right1, on='key')
print(df)

# 4
another = DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                    index=['a', 'c', 'e', 'f'], columns=['New York', 'Oregon'])
df = left2.join([right2, another])
print(df)

df = left2.join([right2, another], how='outer')
print(df)

print('-------------------------')
# 轴向连接
# 1
arr = np.arange(12).reshape((3, 4))
print(arr)

temp = np.concatenate([arr, arr], axis=1)  # 水平方向
print(temp)

# 2
s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])

print(s1)
print(s2)
print(s3)

print(pd.concat([s1, s2, s3]))  # 并集

print(pd.concat([s1, s2, s3], axis=1))  # 外连接

s4 = pd.concat([s1 * 5, s3])

print(s4)

print(pd.concat([s1, s4], axis=1))

print(pd.concat([s1, s4], axis=1, join='inner'))  # 内连接

print(pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']]))  # 指定键

# 3
result = pd.concat([s1, s1, s3], keys=['one', 'two', 'three'])  # 数据集层次索引
print(result)

print(result.unstack())

# 4
print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))  # 并集轴向合并自定义名称

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                columns=['three', 'four'])

print(df1)
print(df2)

print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))

print(pd.concat({'level1': df1, 'level2': df2}, axis=1))

print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2'],
                names=['upper', 'lower']))

# 5
df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

print(df1)
print(df2)

print(pd.concat([df1, df2], ignore_index=True))

print('-------------------------')

# 合并重叠数据
# 1
a = Series([np.nan, 2.5, np.nan, 3.5, 4.5, 7.0],
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b = Series(np.arange(len(a), dtype=np.float64),
           index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan

print(a)

print(b)

# 判断a缺失值，缺失用b，不缺失用a
print(np.where(pd.isnull(a), b, a))

# 2
print(b[:-2].combine_first(a[2:]))  # 同上填充

# 3
df1 = DataFrame({'a': [1., np.nan, 5., np.nan],
                 'b': [np.nan, 2., np.nan, 6.],
                 'c': range(2, 18, 4)})
df2 = DataFrame({'a': [5., 4., np.nan, 3., 7.],
                 'b': [np.nan, 3., 4., 6., 8.]})

df1.combine_first(df2)  # 用df2填补df1

print('-------------------------')
# 重塑层次化索引
# 1
data = DataFrame(np.arange(6).reshape((2, 3)),
                 index=pd.Index(['Ohio', 'Colorado'], name='state'),
                 columns=pd.Index(['one', 'two', 'three'], name='number'))
print(data)

# 转Series
result = data.stack()
print(result)

# 转DataFrame
result.unstack()

result.unstack(0)

result.unstack('state')

# 2
s1 = Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = Series([4, 5, 6], index=['c', 'd', 'e'])
# 纵向合并
data2 = pd.concat([s1, s2], keys=['one', 'two'])
print(data2)

# 转DataFrame
print(data2.unstack())

print(data2.unstack().stack())

# 不丢弃缺失值
print(data2.unstack().stack(dropna=False))

# 3
df = DataFrame({'left': result, 'right': result + 5},
               columns=pd.Index(['left', 'right'], name='side'))
print(df)

print(df.unstack('state'))

print(df.unstack('state').stack('side'))

print('-------------------------')
# 长宽格式的转换
# 1
data = pd.read_csv('./data/macrodata.csv')
# 设定格式
periods = pd.PeriodIndex(year=data.year, quarter=data.quarter, name='date')

data = DataFrame(data.to_records(),
                 columns=pd.Index(['realgdp', 'infl', 'unemp'], name='item'),
                 index=periods.to_timestamp('D', 'end'))

print(data)

ldata = data.stack().reset_index().rename(columns={0: 'value'})
print(ldata)  # 长数据

wdata = ldata.pivot('date', 'item', 'value')
print(wdata)  # 宽数据

# 2
print(ldata[:10])

pivoted = ldata.pivot('date', 'item', 'value')
print(pivoted.head())

ldata['value2'] = np.random.randn(len(ldata))
print(ldata[:10])

pivoted = ldata.pivot('date', 'item')
print(pivoted[:5])

pivoted['value'][:5]

unstacked = ldata.set_index(['date', 'item']).unstack('item')
print(unstacked[:7])

print('-------------------------')
# 移除重复数据
data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})
print(data)

print(data.duplicated())

print(data.drop_duplicates())

data['v1'] = range(7)
print(data)

print(data.drop_duplicates(['k1']))

print('-------------------------')
# 利用函数或映射进行数据转换
# 1
data = DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                           'corned beef', 'Bacon', 'pastrami', 'honey ham',
                           'nova lox'],
                  'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

meat_to_animal = {
    'bacon': 'pig',
    'pulled pork': 'pig',
    'pastrami': 'cow',
    'corned beef': 'cow',
    'honey ham': 'pig',
    'nova lox': 'salmon'
}

data['animal'] = data['food'].map(str.lower).map(meat_to_animal)
print(data)

print(data['food'].map(lambda x: meat_to_animal[x.lower()]))

print('-------------------------')
# 数据标准化
datafile = './data/normalization_data.xls'  # 参数初始化
data = pd.read_excel(datafile, header=None)  # 读取数据

print((data - data.min()) / (data.max() - data.min()))  # 最小-最大规范化
print((data - data.mean()) / data.std())  # 零-均值规范化
print(data / 10 ** np.ceil(np.log10(data.abs().max())))  # 小数定标规范化

print('-------------------------')
# 替换值
data = Series([1., -999., 2., -999., -1000., 3.])
print(data)

print(data.replace(-999, np.nan))

print(data.replace([-999, -1000], np.nan))

print(data.replace([-999, -1000], [np.nan, 0]))

print(data.replace({-999: np.nan, -1000: 0}))

print('-------------------------')
# 重命名轴索引
data = DataFrame(np.arange(12).reshape((3, 4)),
                 index=['Ohio', 'Colorado', 'New York'],
                 columns=['one', 'two', 'three', 'four'])

print(data)

print(data.index.map(str.upper))

data.index = data.index.map(str.upper)
print(data)

print(data.rename(index=str.title, columns=str.upper))

print(data.rename(index={'OHIO': 'INDIANA'},
                  columns={'three': 'peekaboo'}))

print('-------------------------')
# 总是返回DataFrame的引用
_ = data.rename(index={'OHIO': 'INDIANA'}, inplace=True)
print(data)

print('-------------------------')
# 离散化与面元划分
# 1
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

bins = [18, 25, 35, 60, 100]

cats = pd.cut(ages, bins)
print(cats)

print(pd.value_counts(cats))

print(pd.cut(ages, [18, 26, 36, 61, 100], right=False))

group_names = ['Youth', 'YoungAdult', 'MiddleAged', 'Senior']
print(pd.cut(ages, bins, labels=group_names))

data = np.random.rand(20)
print(pd.cut(data, 4, precision=2))

# 2
data = np.random.randn(1000)  # Normally distributed
cats = pd.qcut(data, 4)  # Cut into quartiles
print(cats)

pd.value_counts(cats)

pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.])

print('-------------------------')
# 检测和过滤异常值
# 1
np.random.seed(12345)
data = DataFrame(np.random.randn(1000, 4))
print(data.describe())

col = data[3]
print(col[np.abs(col) > 3])

print(data[(np.abs(data) > 3).any(1)])

# 2
data[np.abs(data) > 3] = np.sign(data) * 3
print(data.describe())

print('-------------------------')
# 排列与随机采样
# 1
df = DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)
print(sampler)
print(df)

print(df.take(sampler))

# 2
print(df.take(np.random.permutation(len(df))[:3]))

# 3
bag = np.array([5, 7, -1, 6, 4])
sampler = np.random.randint(0, len(bag), size=10)
print(sampler)

draws = bag.take(sampler)
print(draws)

print('-------------------------')
# 计算指标与哑变量
# 1
df = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                'data1': range(6)})
print(df)
print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy)

# 2
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('./data/movies.dat', sep='::', header=None,
                       names=mnames)
print(movies[:10])

genre_iter = (set(x.split('|')) for x in movies.genres)
genres = sorted(set.union(*genre_iter))

dummies = DataFrame(np.zeros((len(movies), len(genres))), columns=genres)

for i, gen in enumerate(movies.genres):
    dummies.ix[i, gen.split('|')] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.ix[0])

# 3
np.random.seed(12345)
values = np.random.rand(10)
print(values)

bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.get_dummies(pd.cut(values, bins))

print('-------------------------')
# 线损率属性构造
# 参数初始化
inputfile = './data/electricity_data.xls'  # 供入供出电量数据
outputfile = './data/electricity_data.xls'  # 属性构造后数据文件

data = pd.read_excel(inputfile)  # 读入数据
data[u'线损率'] = (data[u'供入电量'] - data[u'供出电量']) / data[u'供入电量']

data.to_excel(outputfile, index=False)  # 保存结果

print('-------------------------')
# 字符串对象方法
val = 'a,b,  guido'
print(val.split(','))

pieces = [x.strip() for x in val.split(',')]
print(pieces)

first, second, third = pieces
print(first + '::' + second + '::' + third)

print('::'.join(pieces))

print('guido' in val)

print(val.index(','))

print(val.find(':'))

# print(val.index(':'))

print(val.count('a'))

print(val.replace(',', '::'))

print(val.replace(',', ''))

print('-------------------------')
# 正则表达式
# 1
import re

text = "foo    bar\t baz  \tqux"
print(re.split('\s+', text))

regex = re.compile('\s+')
print(regex.split(text))

print(regex.findall(text))

# 2
text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""
pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'
print(pattern)

# re.IGNORECASE 的作用是使正则表达式对大小写不敏感
regex = re.compile(pattern, flags=re.IGNORECASE)

print(regex.findall(text))

m = regex.search(text)
print(m)

print(text[m.start():m.end()])

print(regex.match(text))

print(regex.sub('REDACTED', text))

# 3
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')
print(m.groups())

print(regex.findall(text))

print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))

# 4
regex = re.compile(r"""
     (?P<username>[A-Z0-9._%+-]+)
     @
     (?P<domain>[A-Z0-9.-]+)
     \.
     (?P<suffix>[A-Z]{2,4})""", flags=re.IGNORECASE | re.VERBOSE)

m = regex.match('wesm@bright.net')
print(m.groupdict())

# pandas中矢量化的字符串函数
data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}
data = Series(data)

print(data)

print(data.isnull())

print(data.str.contains('gmail'))

print(pattern)

print(data.str.findall(pattern, flags=re.IGNORECASE))

matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches)

print(matches.str.get(1))

print(matches.str[0])

print(data.str[:5])

print('-------------------------')
# 示例：USDA食品数据库
'''
{
  "id": 21441,
  "description": "KENTUCKY FRIED CHICKEN, Fried Chicken, EXTRA CRISPY,
Wing, meat and skin with breading",
  "tags": ["KFC"],
  "manufacturer": "Kentucky Fried Chicken",
  "group": "Fast Foods",
  "portions": [
    {
      "amount": 1,
      "unit": "wing, with skin",
      "grams": 68.0
    },

    ...
  ],
  "nutrients": [
    {
      "value": 20.8,
      "units": "g",
      "description": "Protein",
      "group": "Composition"
    },

    ...
  ]
}
'''

import json

db = json.load(open('./data/foods-2011-10-03.json'))
print(len(db))

print(db[0].keys())

print(db[0]['nutrients'][0])

nutrients = DataFrame(db[0]['nutrients'])
print(nutrients[:7])

info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)

print(info[:5])
print(info)

print(pd.value_counts(info.group)[:10])

nutrients = []

for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)

nutrients = pd.concat(nutrients, ignore_index=True)

print(nutrients)

print(nutrients.duplicated().sum())

nutrients = nutrients.drop_duplicates()

col_mapping = {'description': 'food',
               'group': 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)
print(info)

col_mapping = {'description': 'nutrient',
               'group': 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)
print(nutrients)

ndata = pd.merge(nutrients, info, on='id', how='outer')

print(ndata)

print(ndata.ix[30000])

result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
print(result['Zinc, Zn'].order().plot(kind='barh'))

by_nutrient = ndata.groupby(['nutgroup', 'nutrient'])

get_maximum = lambda x: x.xs(x.value.idxmax())
get_minimum = lambda x: x.xs(x.value.idxmin())

max_foods = by_nutrient.apply(get_maximum)[['value', 'food']]

# make the food a little smaller
max_foods.food = max_foods.food.str[:50]

print(max_foods.ix['Amino Acids']['food'])
