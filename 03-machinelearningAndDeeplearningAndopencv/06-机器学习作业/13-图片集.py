from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
faces = fetch_lfw_people(min_faces_per_person=10)
#取出我们需要用到的数据
X = faces.data
print(faces.images.shape)
print(faces.data.shape)

#创建画布和子图对象
#横纵长度为4和5的画布
fig, axes = plt.subplots(4, 5,figsize=(8, 4), subplot_kw = {"xticks":[],"yticks":[]}) #不要显示坐标轴
#这里采用enumerate函数对axes进行变化绘制（这里是将二位数据拉成一维）
for i, ax in enumerate(axes.flat):
	#显示图片
    ax.imshow(faces.images[i, :, :], cmap='gray')
plt.savefig(r"./images/1.png")

#原本有2900维，我们现在来降到150维
pca = PCA(10).fit(X)
V = pca.components_
fig, axes = plt.subplots(10, 15, figsize=(20, 8), subplot_kw={"xticks": [], "yticks": []})
# for i, ax in enumerate(axes.flat):
#     ax.imshow(V[i, :].reshape(6, 4), cmap="gray")
#降维后的数据
X_dr = pca.transform(X)
#还原的数据
X_inverse = pca.inverse_transform(X_dr)
#可视化
fig, axes = plt.subplots(2, 10, subplot_kw={'xticks': [], 'yticks': []})
for i in range(10):
    axes[0, i].imshow(X[i, :].reshape(62, 47), cmap='binary_r')
    axes[1, i].imshow(X_inverse[i, :].reshape(62, 47), cmap='binary_r')
plt.savefig(r"./images/4.png")

