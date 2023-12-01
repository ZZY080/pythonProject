from sklearn.datasets import  load_wine
from sklearn.ensemble import  RandomForestClassifier
from sklearn.model_selection import  train_test_split
from sklearn.metrics import  accuracy_score

# 读取数据
data=load_wine()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.3)
model=RandomForestClassifier()
model.fit(X_train,y_train)
pred=model.predict(X_test)
score=accuracy_score(y_test,pred)
print(score)