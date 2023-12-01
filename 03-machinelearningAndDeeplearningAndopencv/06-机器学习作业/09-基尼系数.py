import  numpy as np
def calcGini(feature, label):
    p1=np.mean(label)
    p0=1-p1
    result=1-p0**2-p1**2
    return result
feature=[[0 ,1],
 [1 ,0],
 [1 ,2],
 [0, 0],
 [1 ,1]]
label=[0 ,1, 0, 0 ,1]
result=calcGini(feature,label)
print(result)