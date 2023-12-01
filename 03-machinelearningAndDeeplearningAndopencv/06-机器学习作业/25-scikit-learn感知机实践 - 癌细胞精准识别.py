from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import  train_test_split
from sklearn.linear_model._perceptron import Perceptron
from sklearn.metrics import  accuracy_score
import pandas as pd
data=load_breast_cancer()

X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,train_size=0.8)

model=Perceptron(eta0=8,max_iter=200)
model.fit(X_train,y_train)
pred=model.predict(X_test)
print(accuracy_score(y_test,pred))
data_DataFrame=pd.DataFrame({"result":pred})
data_DataFrame.to_csv('./data/result.csv',index=False,header=True)

