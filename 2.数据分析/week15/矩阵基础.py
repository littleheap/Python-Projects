# -*- coding: utf-8 -*-

# 协方差矩阵
import numpy as np

X = [[2, 0, -1.4],
     [2.2, 0.2, -1.5],
     [2.4, 0.1, -1],
     [1.9, 0, -1.2]]

print(np.cov(np.array(X).T))

# 特征值与特征向量
w, v = np.linalg.eig(np.array([[1, -2], [2, -3]]))

print('特征值：{}\n特征向量：{}'.format(w, v))

a = [[-0.27, -0.3],
     [1.23, 1.3],
     [0.03, 0.4],
     [-0.67, 0.6],
     [-0.87, 0.6],
     [0.63, 0.1],
     [-0.67, -0.7],
     [-0.87, -0.7],
     [1.33, 1.3],
     [0.13, -0.2]]

b = [[0.73251454], [0.68075138]]

print(np.dot(a, b))

# 鸢尾花数据集的降维
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

data = load_iris()
y = data.target
X = data.data
pca = PCA(n_components=2)
reduced_X = pca.fit_transform(X)

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
for i in range(len(reduced_X)):
    if y[i] == 0:
        red_x.append(reduced_X[i][0])
        red_y.append(reduced_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_X[i][0])
        blue_y.append(reduced_X[i][1])
    else:
        green_x.append(reduced_X[i][0])
        green_y.append(reduced_X[i][1])
plt.scatter(red_x, red_y, c='r', marker='x')
plt.scatter(blue_x, blue_y, c='b', marker='D')
plt.scatter(green_x, green_y, c='g', marker='.')
plt.show()
