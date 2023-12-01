import  matplotlib.pyplot as plt
from sklearn.decomposition import  PCA
from matplotlib.pyplot import  imread
import  numpy as np

img=imread("")
img=img.astype(np.uint8)
img=img/255
img=img.mean(axis=2)
plt.imshow(img,cmap="gray")

def transform(percentage):
    percentage=percentage/100
    pca=PCA(n_components=percentage).fit(img)
    transforms=pca.transforms(img)
    p



