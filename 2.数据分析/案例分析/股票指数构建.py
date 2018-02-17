import pandas as pd
from datetime import datetime
from sklearn.decomposition import PCA, FactorAnalysis
import matplotlib.pyplot as plt

# 读入数据
data = pd.read_csv("stock_prices.csv")
data['Date'] = [datetime.strptime(x, '%Y-%m-%d') for x in data.Date]
data = data[data['Stock'] != 'DDR']
ndat = data.pivot('Date', 'Stock', 'Close')
ndat.head()
ndat = ndat.dropna()

# 协方差矩阵
cor_mat = ndat.corr()
print(cor_mat)

# 主成分分析
pca = PCA()
reduced_X = pca.fit_transform(ndat)
print(pca.explained_variance_ratio_)

pca2 = PCA(n_components=1)
market = pca2.fit_transform(ndat)

# 与道琼斯指数比较
dji = pd.read_csv("DJI.csv")
dji = dji.dropna()
dji['Date'] = [datetime.strptime(x, '%Y/%m/%d') for x in dji.Date]
dji.head()
dji_sub = dji[dji.Date.isin(ndat.index)]
dji_close = dji_sub['Close']

fig = plt.figure()
plt.scatter(dji_close, market, color='blue')
plt.show()

dji_close2 = (dji_close - dji_close.mean()) / dji_close.std()
market2 = -(market - market.mean()) / market.std()
fig = plt.figure()
plt.plot(market2, color='red')
plt.plot(dji_close2, color='blue')

# 因子分析
fa = FactorAnalysis(n_components=1)
market3 = fa.fit_transform(ndat)

fig = plt.figure()
plt.scatter(dji_close, market3, color='blue')
plt.show()

market4 = -(market3 - market3.mean()) / market3.std()
fig = plt.figure()
plt.plot(market4, c="g")
plt.plot(market2, c="r")
plt.plot(dji_close2, c='b')
