from numpy import *
import numpy as np
import pandas as pd

# 线性回归
# 读取数据
data = pd.read_csv('Advertising.csv', index_col=0)

print('\n')
print('data head : ')
print(data.head())  # 数据前5行

print('\n')
print('data tail : ')
print(data.tail())  # 数据后5行

# 画散点图
import seaborn as sns
import matplotlib.pyplot as plt

# # 单显示数据
# sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', size=7, aspect=0.8)
#
# # 加上回归线
# sns.pairplot(data, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', size=7, aspect=0.8, kind='reg')
#
# x = data[['TV', 'Radio', 'Newspaper']]
# y = data['Sales']
# plt.figure(figsize=(9, 12))
# plt.subplot(311)
# plt.plot(data['TV'], y, 'ro')
# plt.title('TV')
# plt.grid()
# plt.subplot(312)
# plt.plot(data['Radio'], y, 'g^')
# plt.title('Radio')
# plt.grid()
# plt.subplot(313)
# plt.plot(data['Newspaper'], y, 'b*')
# plt.title('Newspaper')
# plt.grid()
# plt.tight_layout()
# plt.show()

# 计算相关系数矩阵
print('\n')
print('相关矩阵：')
print(data.corr())

# 构建X、Y数据集
X = data[['TV', 'Radio', 'Newspaper']]
print('\n')
print('X-head : ')
print(X.head())

y = data['Sales']
print('\n')
print('Y-head : ')
print(y.head())


# 根据系数矩阵公式计算
def standRegres(xArr, yArr):
    # 转化为矩阵
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:  # 判断行列式是不是0，是奇异矩阵的话就不能求逆
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)  # I是矩阵的逆
    return ws


# 求解回归方程系数
X2 = X
X2['intercept'] = [1] * 200  # 原始自变量数据增加一列全1的截距项，变为4列
print('\n')
print('根据系数矩阵公式计算的四个参数：\n', standRegres(X2, y))

# 利用现有库求解
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()

linreg.fit(X, y)

print('\n')
print('库函数计算的参数：', linreg.coef_)
print('库函数计算的截距：', linreg.intercept_)

print(zip(['TV', 'Radio', 'Newspaper'], linreg.coef_))

# 测试集和训练集的构建，交叉验证
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg.fit(X_train, y_train)

# 结果
print('\n')

print('交叉验证计算的系数：', linreg.coef_)

print('交叉验证计算的截距：', linreg.intercept_)

print(zip(['TV', 'Radio', 'Newspaper'], linreg.coef_))

# 预测
y_pred = linreg.predict(X_test)

# 误差评估
from sklearn import metrics

print('\n')
print('三元参数模型评估：')

# 误差取绝对值的均值
print("MAE:", metrics.mean_absolute_error(y_test, y_pred))

# 误差的平方的均值
print("MSE:", metrics.mean_squared_error(y_test, y_pred))

# MSE的开方
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 只选择电视和广播的数据训练，报纸作用不大剔除
feature_cols = ['TV', 'Radio']

X = data[feature_cols]
y = data.Sales

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg.fit(X_train, y_train)

y_pred = linreg.predict(X_test)

print('\n')
print('二元参数模型评估：')

# 对比模型性能
print("MAE:", metrics.mean_absolute_error(y_test, y_pred))

print("MSE:", metrics.mean_squared_error(y_test, y_pred))

print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
