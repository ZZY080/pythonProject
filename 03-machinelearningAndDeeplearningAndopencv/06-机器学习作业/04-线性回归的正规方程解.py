import  numpy as np
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import  accuracy_score
# 损失函数
def mse_score(y_predict,y_test):
    mse=np.mean((y_test-y_predict)**2)
    return mse
def r2_score(y_predict,y_test):
    r2=1-mse_score(y_predict,y_test)/np.var(y_test)
    return r2

# 线性回归
class LinearRegression:
    def __init__(self):
        # 初始化线性回归模型
        self.theta=None

    def fit_normal(self,X,y):
        ones=np.ones([X.shape[0],1])
        X=np.concatenate((ones,X),axis=1)
        XT=X.T
        XTX=XT.dot(X)
        XTX_1=np.linalg.inv(XTX)
        XTY=XT.dot(y)
        self.theta=XTX_1.dot(XTY)
        return self.theta
    def predict(self,X_test):
        ones=np.ones([X_test.shape[0],1])
        X_test=np.concatenate((ones,X_test),axis=1)
        result=X_test.dot(self.theta)
        return  result
# 加载数据
data=load_boston()
X=data.data
y=data.target
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4)
model=LinearRegression()
model.fit_normal(X_train,y_train)
pred=model.predict(X_test)
print(pred)
# score=accuracy_score(y_test,pred)
# print(score)






