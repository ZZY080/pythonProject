from sklearn.datasets import  load_wine
from  sklearn.cluster import  KMeans
import matplotlib.pyplot as plt
data=load_wine()
X=data.data[:,[0,9]]

# 三个簇
n_clusters=3
# 模型加载
model=KMeans(n_clusters=n_clusters)
# 模型训练
model.fit(X)
# 模型预测
pred=model.predict(X)
# 模型评估
print(len(pred))

plt.show()


