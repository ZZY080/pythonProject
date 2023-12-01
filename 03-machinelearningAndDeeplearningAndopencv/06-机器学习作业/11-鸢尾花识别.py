from sklearn.tree import  DecisionTreeClassifier
from sklearn.datasets import  load_iris
import numpy as np
import  pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score

data=load_iris()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.3)
modle=DecisionTreeClassifier()
modle.fit(X_train,y_train)
predict=modle.predict(X_test)
result=accuracy_score(y_test,predict)
print(result)

