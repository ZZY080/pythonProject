import numpy as np
from sklearn.linear_model import  LogisticRegression

# np.r_ 拼接数据 np.r_[[1,2,3],[4,5,6]] ==> [1 2 3 4 5 6]
X_train=np.r_[np.random.normal(3,1,size=50),np.random.normal(-1,1,size=50)].reshape((100,-1))

# 生成50个全0和全1数组并拼接
y_train=np.r_[np.ones(50),np.zeros(50)]

model=LogisticRegression()
model.fit(X_train,y_train)
result=model.predict([[0],[1],[2]])
# result2=model.predict_proba([[0],[1],[2]])[:,1]
# print(result2)