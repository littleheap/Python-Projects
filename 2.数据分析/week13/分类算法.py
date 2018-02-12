# -*- coding: utf-8 -*-

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

# knn最邻近算法
inputfile = 'sales_data.xls'
data = pd.read_excel(inputfile, index_col=u'序号')  # 导入数据

# 数据是类别标签，要将它转换为数据
# 用1来表示“好”、“是”、“高”这三个属性，用-1来表示“坏”、“否”、“低”
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1
x = data.iloc[:, :3].as_matrix().astype(int)  # 前3列作为特征值
y = data.iloc[:, 3].as_matrix().astype(int)  # 第4列作为输出

# 拆分训练数据与测试数据
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# 训练KNN分类器
clf = KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print('x_test : \n', x_test)
print('answer : \n', answer)
print('y_test : \n', y_test)
print('answer == y_test : \n', np.mean(answer == y_test))

# 准确率
precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
print('report : ', classification_report(y_test, answer, target_names=['高', '低']))

print('-----------------------------')
# 贝叶斯分类器
# 训练贝叶斯分类器
clf = BernoulliNB()
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print('x_test : \n', x_test)
print('answer : \n', answer)
print('y_test : \n', y_test)
print('answer == y_test : \n', np.mean(answer == y_test))
print('report : ', classification_report(y_test, answer, target_names=['低', '高']))

print('-----------------------------')
# 决策树
from sklearn.tree import DecisionTreeClassifier as DTC

dtc = DTC(criterion='entropy')  # 建立决策树模型，基于信息熵
dtc.fit(x_train, y_train)  # 训练模型

# 导入相关函数，可视化决策树。
# 导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO

with open("tree.dot", 'w') as f:
    f = export_graphviz(dtc, out_file=f)

# 测试结果
answer = dtc.predict(x_test)
print('x_test : \n', x_test)
print('answer : \n', answer)
print('y_test : \n', y_test)
print('answer == y_test : \n', np.mean(answer == y_test))
print('report : ', classification_report(y_test, answer, target_names=['低', '高']))

print('-----------------------------')
# SVM
from sklearn.svm import SVC

clf = SVC()
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print('x_test : \n', x_test)
print('answer : \n', answer)
print('y_test : \n', y_test)
print('answer == y_test : \n', np.mean(answer == y_test))
print('report : ', classification_report(y_test, answer, target_names=['低', '高']))
