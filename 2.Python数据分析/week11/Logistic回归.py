# -*- coding: utf-8 -*-

# 逻辑回归 自动建模
import pandas as pd

# 参数初始化
filename = 'bankloan.xls'  # 银行贷款客户数据，700 * (8 + 1)
data = pd.read_excel(filename)
print('data-head : ')
print(data)

x = data.iloc[:, :8].as_matrix()  # 取前8列作为特征矩阵
y = data.iloc[:, 8].as_matrix()  # 取第9列作为结果矩阵
print('\n')
print('X : ', x)
print('Y : ', y)

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR

rlr = RLR()  # 建立随机逻辑回归模型，筛选变量
rlr.fit(x, y)  # 训练模型
support = list(rlr.get_support())
support.append(False)
print('\n')
print('特征筛选结果：', support)  # 获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
print(u'有效特征为：%s' % ','.join(data.columns[support]))

x = data[data.columns[support]].as_matrix()  # 筛选好特征，重新构建数据集

lr = LR()  # 建立逻辑回归模型
lr.fit(x, y)  # 用筛选后的特征数据来训练模型
print('\n')
print(u'Logistic模型的平均正确率为：%s' % lr.score(x, y))  # 给出模型的平均正确率，本例为81.4%

# 非线性回归
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import metrics

x = pd.DataFrame([1.5, 2.8, 4.5, 7.5, 10.5, 13.5, 15.1, 16.5, 19.5, 22.5, 24.5, 26.5])
y = pd.DataFrame([7.0, 5.5, 4.6, 3.6, 2.9, 2.7, 2.5, 2.4, 2.2, 2.1, 1.9, 1.8])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(x, y)
fig.show()

from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(x, y)

print('\n')
print('线性回归的Coefficients: ', linreg.coef_)

y_pred = linreg.predict(x)

print("MSE: ", metrics.mean_squared_error(y, y_pred))

print('Variance score: %.2f' % linreg.score(x, y))

# 多项式模型
x1 = x
x2 = x ** 2
x1['x2'] = x2

linreg = LinearRegression()
linreg.fit(x1, y)

print('\n')
print('非线性回归的Coefficients: ', linreg.coef_)

y_pred = linreg.predict(x)

print("MSE:", metrics.mean_squared_error(y, y_pred))

# 对数模型
x2 = pd.DataFrame(np.log(x[0]))

linreg = LinearRegression()
linreg.fit(x2, y)

print('\n')
print('对数模型的Coefficients: ', linreg.coef_)

y_pred = linreg.predict(x2)
print("MSE:", metrics.mean_squared_error(y, y_pred))

# 指数模型
y2 = pd.DataFrame(np.log(y))  # 对因变量求对数

linreg = LinearRegression()
linreg.fit(pd.DataFrame(x[0]), y2)

print('\n')
print('指数模型的Coefficients: ', linreg.coef_)

y_pred = linreg.predict(pd.DataFrame(x[0]))

print("MSE:", metrics.mean_squared_error(y2, y_pred))

# 幂函数模型的

linreg = LinearRegression()
linreg.fit(x2, y2)

print('\n')
print('幂函数模型的Coefficients: \n', linreg.coef_)

y_pred = linreg.predict(x2)

print("MSE:", metrics.mean_squared_error(y2, y_pred))
