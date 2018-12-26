# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import sys
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

filename = 'telco.xls'
data = pd.read_excel(filename)
data.head()

x = data.iloc[:, :37].as_matrix()
y = data.iloc[:, 37].as_matrix()

from sklearn.linear_model import LogisticRegression as LR

lr = LR()  # 建立逻辑回归模型
lr.fit(x, y)  # 用筛选后的特征数据来训练模型
print(u'逻辑回归模型训练结束。')
print(u'模型的平均正确率为：%s' % lr.score(x, y))  # 给出模型的平均正确率，本例为77.8%


def cm_plot(y, yp):
    from sklearn.metrics import confusion_matrix  # 导入混淆矩阵函数

    cm = confusion_matrix(y, yp)  # 混淆矩阵

    import matplotlib.pyplot as plt  # 导入作图库
    plt.matshow(cm, cmap=plt.cm.Greens)  # 画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
    plt.colorbar()  # 颜色标签

    for x in range(len(cm)):  # 数据标签
        for y in range(len(cm)):
            plt.annotate(cm[x, y], xy=(x, y), horizontalalignment='center', verticalalignment='center')

    plt.ylabel('True label')  # 坐标轴标签
    plt.xlabel('Predicted label')  # 坐标轴标签
    return plt


from sklearn.cross_validation import train_test_split

p = 0.2  # 设置测试数据比例
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=p)

from sklearn.tree import DecisionTreeClassifier  # 导入决策树模型

treefile = 'd:/data/tree.pkl'  # 模型输出名字
tree = DecisionTreeClassifier()  # 建立决策树模型
tree.fit(x_train, y_train)  # 训练

# 保存模型
from sklearn.externals import joblib

joblib.dump(tree, treefile)

cm_plot(y_train, tree.predict(x_train)).show()  # 显示混淆矩阵可视化结果
# 注意到Scikit-Learn使用predict方法直接给出预测结果。

from sklearn.metrics import roc_curve  # 导入ROC曲线函数

fpr, tpr, thresholds = roc_curve(y_test, tree.predict_proba(x_test)[:, 1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label='ROC of CART', color='green')  # 作出ROC曲线
plt.xlabel('False Positive Rate')  # 坐标轴标签
plt.ylabel('True Positive Rate')  # 坐标轴标签
plt.ylim(0, 1.05)  # 边界范围
plt.xlim(0, 1.05)  # 边界范围
plt.legend(loc=4)  # 图例
plt.show()  # 显示作图结果

# 训练KNN分类器
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report

clf = KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean(answer == y_test))

# 准确率
precision, recall, thresholds = precision_recall_curve(y_train, clf.predict(x_train))
print(classification_report(y_test, answer, target_names=['高', '低']))

# 贝叶斯分类器
# 训练贝叶斯分类器
from sklearn.naive_bayes import BernoulliNB

clf = BernoulliNB()
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean(answer == y_test))
print(classification_report(y_test, answer, target_names=['低', '高']))

from sklearn.svm import SVC

clf = SVC()
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean(answer == y_test))
print(classification_report(y_test, answer, target_names=['低', '高']))
