from sklearn.datasets import  load_iris
import cv2 as cv
import pandas as pd
data=load_iris()
pd.set_option('display.colheader_justify', 'center')
X=pd.DataFrame(data.data,columns=data.feature_names)
# 自定义目标变量名为species
y=pd.DataFrame(data.target,columns=['Species'])
df=pd.concat([X,y],axis=1)
# print(df.head())
print(data.feature_names)
print(df.loc[:,['sepal length (cm)','sepal width (cm)']])
# print(df[['sepal length (cm)','sepal width (cm)']])
