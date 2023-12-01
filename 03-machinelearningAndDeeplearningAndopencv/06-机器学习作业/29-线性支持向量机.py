from sklearn.svm import  LinearSVC
from sklearn.datasets import  load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
data=load_iris()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,train_size=0.8)
model=LinearSVC(dual=False,)
model.fit(X_train,y_train)
pred=model.predict((X_test))
print(accuracy_score(y_test,pred))
