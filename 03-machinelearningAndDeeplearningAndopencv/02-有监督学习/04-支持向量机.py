from sklearn.svm import  LinearSVC
from sklearn.datasets import  make_blobs
from sklearn.model_selection import  train_test_split
from  sklearn.metrics import  accuracy_score

centers=[(-1,-0.125),(0.5,0.5)]
# make_blobs 数据集中 特征数据集50 目标数据集50
X,y=make_blobs(n_samples=50,n_features=2,centers=centers,cluster_std=0.3)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.5)
model=LinearSVC()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
res=accuracy_score(y_test,y_pred)
print(res)