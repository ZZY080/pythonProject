from sklearn.datasets import  load_iris
from sklearn.neural_network import  MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
data=load_iris()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,train_size=0.7)
model=MLPClassifier(solver='lbfgs',hidden_layer_sizes=400,learning_rate_init=0.9)
model.fit(X_train,y_train)
pred=model.predict(X_test)
score=accuracy_score(y_test,pred)
print(score)