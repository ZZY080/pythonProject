import numpy as np
class KNNClassifier:
    def __init__(self,k):
        self.k=k
        self.train_feature=None
        self.train_label=None

    def fit(self,feature,label):
        self.train_feature=feature
        self.train_label=label

    def predict(self,feature):
        pass

a=np.array([[6,2,3,4],[4,5,6,7]])
b=np.array([1,2,3,4])
print(a-b)
print(np.sum(a-b,axis=1))
print(np.argsort(np.sum(a-b,axis=1)))
print(np.argsort([4,5,6,1]))



