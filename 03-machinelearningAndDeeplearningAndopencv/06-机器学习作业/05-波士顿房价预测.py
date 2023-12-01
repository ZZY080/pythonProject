from sklearn.datasets import  load_boston
from sklearn.linear_model import  LinearRegression
from sklearn.model_selection import  train_test_split

data=load_boston()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,test_size=0.3)
model=LinearRegression()
model.fit(X_train,y_train)
pred=model.predict(X_test)
with open('./data/result.csv','w+',encoding='utf8') as f:
    for i in pred:
        f.write(str(i)+'\n')