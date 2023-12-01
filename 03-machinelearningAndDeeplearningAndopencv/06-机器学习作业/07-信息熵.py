import  numpy as np
def entropy(p):
    result=-1.0*p*np.log2(p)
    return result
def calcEntropy(feature,label):
    p1=np.mean(label)
    p0=1-p1
    result=entropy(p0)+entropy(p1)
    return result
feature=[[0 ,1],[1, 0],[1 ,2],[0, 0],[1 ,1]]
label=[0, 1 ,0 ,0 ,1]
result=calcEntropy(feature,label)
print(result)