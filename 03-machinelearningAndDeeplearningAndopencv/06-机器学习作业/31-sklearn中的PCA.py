from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import  train_test_split
from sklearn.metrics import  accuracy_score
from sklearn.datasets import  load_breast_cancer

data=load_breast_cancer()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,train_size=0.8)
n_components=14
model=PCA(n_components=n_components)
model.fit(X_train)
X_train=model.transform(X_train)

model=PCA(n_components=n_components)
model.fit(X_test)
X_test=model.transform(X_test)

model=RandomForestClassifier()
model.fit(X_train,y_train)
pred=model.predict(X_test)
print(accuracy_score(y_test,pred))