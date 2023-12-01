from sklearn.cluster import KMeans
from sklearn.datasets import  load_iris
data=load_iris()
n_clusters=3 # 将簇的数量设置为3
model=KMeans(n_clusters=n_clusters)
model.fit(data.data)
print(model.labels_) # 各数据点所属的簇
print(model.cluster_centers_) # g通过fit计算得到的重心