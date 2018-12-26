import pandas as pd
from pandas import Series, DataFrame

# 数据读取
# 读取文本格式数据
df = pd.read_csv('d:data/ex1.csv')
print(df)

# 另一种方法数据读取
pd.read_table('d:data/ex1.csv', sep=',')

# 不需要以表头方式读取第一行
df = pd.read_csv('d:data/ex2.csv', header=None)
print(df)
# 自定义添加表头
df = pd.read_csv('d:data/ex2.csv', names=['a', 'b', 'c', 'd', 'message'])
print(df)

names = ['a', 'b', 'c', 'd', 'message']
df = pd.read_csv('d:data/ex2.csv', names=names, index_col='message')
print(df)

# 归一化数据
parsed = pd.read_csv('d:data/csv_mindex.csv', index_col=['key1', 'key2'])
print(parsed)

# 正则表达式读取数据
list(open('d:data/ex3.txt'))
result = pd.read_table('d:data/ex3.txt', sep='\s+')
print(result)

# 略过指定行
df = pd.read_csv('d:data/ex4.csv', skiprows=[0, 2, 3])
print(df)

# 缺失值情况
result = pd.read_csv('d:data/ex5.csv')
print(result)
print(pd.isnull(result))

# 缺失值处理
result = pd.read_csv('d:data/ex5.csv', na_values=['NULL'])
print(result)

sentinels = {'message': ['foo', 'NA'], 'something': ['two']}
pd.read_csv('d:data/ex5.csv', na_values=sentinels)

# 逐行读取文本文件
result = pd.read_csv('d:data/ex6.csv')
# print(result)

# 读取前五行
df = pd.read_csv('d:data/ex6.csv', nrows=5)
print(df)

# 分块读取
chunker = pd.read_csv('d:data/ex6.csv', chunksize=1000)
print(chunker)

chunker = pd.read_csv('d:data/ex6.csv', chunksize=1000)
print(chunker)

# 累计统计
tot = Series([])
for piece in chunker:
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values()
print(tot[:10])

# 文件写出
data = pd.read_csv('d:data/ex5.csv')
print(data)
data.to_csv('d:data/out.csv')

import sys
import numpy as np

# 设置分隔符
df = data.to_csv(sys.stdout, sep='|')
print(df)

# 设置缺省值
df = data.to_csv(sys.stdout, na_rep='NULL')
print(df)

# 省略行列标签
df = data.to_csv(sys.stdout, index=False, header=False)
print(df)

# 指定列
df = data.to_csv(sys.stdout, index=False, columns=['a', 'b', 'c'])
print(df)

# 循环写操作
dates = pd.date_range('1/1/2000', periods=7)
ts = Series(np.arange(7), index=dates)
ts.to_csv('tseries.csv')

df = Series.from_csv('tseries.csv', parse_dates=True)
print(df)

print('-----------------------------------')
print('-----------------------------------')
# 手工处理分隔符格式
import csv

f = open('d:data/ex7.csv')

reader = csv.reader(f)

for line in reader:
    print(line)

# 字典处理，数据对齐
lines = list(csv.reader(open('d:data/ex7.csv')))
header, values = lines[0], lines[1:]
data_dict = {h: v for h, v in zip(header, zip(*values))}
print(data_dict)


class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = ';'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


with open('mydata.csv', 'w') as f:
    writer = csv.writer(f, dialect=my_dialect)
    writer.writerow(('one', 'two', 'three'))
    writer.writerow(('1', '2', '3'))
    writer.writerow(('4', '5', '6'))
    writer.writerow(('7', '8', '9'))
df = pd.read_table('mydata.csv', sep=';')
print(df)

print('-----------------------------------')
print('-----------------------------------')
# Excel数据
# 生成xls工作薄
import xlwt, xlrd

path = 'd:data/'

wb = xlwt.Workbook()
print(wb)

wb.add_sheet('first_sheet', cell_overwrite_ok=True)
print(wb.get_active_sheet())

ws_1 = wb.get_sheet(0)
print(ws_1)

ws_2 = wb.add_sheet('second_sheet')

data = np.arange(1.0, 65.0).reshape((8, 8))
print(data)

# 写入：行 || 列 || 值
ws_1.write(0, 0, 100)

# 循环写入
for c in range(data.shape[0]):
    for r in range(data.shape[1]):
        ws_1.write(r, c, data[c, r])
        ws_2.write(r, c, data[r, c])

wb.save(path + 'workbook.xls')

# 生成xlsx工作薄

# 从工作薄中读取
book = xlrd.open_workbook(path + 'workbook.xls')
print(book)

book.sheet_names()

# 获取工作表
sheet_1 = book.sheet_by_name('first_sheet')
sheet_2 = book.sheet_by_index(1)
print(sheet_1)
print(sheet_2.name)

# 工作表行列数
print(sheet_1.ncols, sheet_1.nrows)

# 获取工作空间某一格数据
cl = sheet_1.cell(0, 0)
print(cl.value)
print(cl.ctype)

print(sheet_2.row(3))

print(sheet_2.col(3))

print(sheet_1.col_values(3, start_rowx=3, end_rowx=7))

print(sheet_1.row_values(3, start_colx=3, end_colx=7))
#
for c in range(sheet_1.ncols):
    for r in range(sheet_1.nrows):
        print('%i' % sheet_1.cell(r, c).value)
    print

# 使用pandas读取
xls_file = pd.ExcelFile(path + 'workbook.xls')
table = xls_file.parse('first_sheet')
print(table)
table = xls_file.parse('second_sheet')
print(table)

print('-----------------------------------')
print('-----------------------------------')
# JSON数据

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": [{"name": "Scott", "age": 25, "pet": "Zuko"},
              {"name": "Katie", "age": 33, "pet": "Cisco"}]
}
"""

import json

result = json.loads(obj)
print(result)

asjson = json.dumps(result)

siblings = DataFrame(result['siblings'], columns=['name', 'age'])
print(siblings)

print('-----------------------------------')
print('-----------------------------------')
# 二进制数据格式
# pickle
frame = pd.read_csv('d:data/ex1.csv')
print(frame)
frame.to_pickle('d:data/frame_pickle')

df = pd.read_pickle('d:data/frame_pickle')
print(df)

# # HDF5格式
# store = pd.HDFStore('mydata.h5')
# store['obj1'] = frame
# store['obj1_col'] = frame['a']
# store
#
# store['obj1']
#
# store.close()
# os.remove('mydata.h5')

print('-----------------------------------')
print('-----------------------------------')
# 使用HTML和Web API
import requests

url = 'https://api.github.com/repos/pydata/pandas/milestones/28/labels'
resp = requests.get(url)
print(resp)

data = json.loads(resp.text)

issue_labels = DataFrame(data)
print(issue_labels)

print('-----------------------------------')
print('-----------------------------------')
# 使用数据库
import sqlite3

query = """
CREATE TABLE test
(a VARCHAR(20), b VARCHAR(20),
 c REAL,        d INTEGER
);"""

con = sqlite3.connect(':memory:')
con.execute(query)
con.commit()

data = [('Atlanta', 'Georgia', 1.25, 6),
        ('Tallahassee', 'Florida', 2.6, 3),
        ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

con.executemany(stmt, data)
con.commit()

cursor = con.execute('SELECT * FROM test')
rows = cursor.fetchall()
print(rows)

DataFrame(rows, columns=zip(*cursor.description)[0])

import pandas.io.sql as sql

result = sql.read_sql('select * from test', con)
print(result)
