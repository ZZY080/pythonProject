from sklearn.neighbors import  KNeighborsClassifier
from sklearn.datasets import  make_moons
from sklearn.model_selection import  train_test_split
from sklearn.metrics import  accuracy_score

X,y=make_moons(noise=0.3)
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)
model=KNeighborsClassifier()
model.fit(X_train,y_train)
pred=model.predict(X_test)
score=accuracy_score(y_test,pred)
print(score)