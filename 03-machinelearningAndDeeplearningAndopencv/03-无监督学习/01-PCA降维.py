from sklearn.decomposition import  PCA
from sklearn.datasets import  load_iris
data=load_iris()
n_components=2 # 减少后的维度为2
model=PCA(n_components=n_components)
model.fit(data.data)
print(model.transform(data.data))