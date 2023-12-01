import  numpy as np

class Perception(object):
    def __init__(self,learning_rate=0.01,max_iter=200):
        self.lr=learning_rate
        self.max_iter=max_iter

    def fit(self,data,label):
        self.w=np.array([1]*data.shape[1])
        self.b=np.array([1])
        i=0
        while i<self.max_iter:
            flag=True
            for j in range(len(label)):
                if label[j]*(np.inner(self.w,data[j])+self.b)<=0:
                    flag=False
                    self.w+=self.lr*(label[j]*data[j])
                    self.b+=self.lr*label[j]
            if flag:
                break
            i+=1
    def predict(self,data):
        y=np.inner(data,self.w)+self.b
        for i in range(len(y)):
            if y[i]>=0:
                y[i]=1
            else:
                y[i]=-1
        predict=y
        return predict

a=np.array(
    [
        [1,2,3,4],
        [2,3,4,5]
    ]
)
b=np.array([2,2,2,2])

result=np.inner(a,b)
print(result)






