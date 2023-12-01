import  numpy as np
def entry_log2(p):
    result=-1.0*np.log2(p)*p
    return result
def totalentropy(label):
    p1 = np.mean(label)
    p0 = 1 - p1
    result=entry_log2(p0)+entry_log2(p1)
    return result
def calcInfoGain(feature, label, index):
    totalentropyresult=totalentropy(label)
    sort_type=feature[:,index]
    sort_type0=sort_type[sort_type==0]
    sort_type1=sort_type[sort_type==1]
feature=[[0 ,1],
         [1 ,0],
         [1 ,2],
         [0, 0],
         [1, 1]]
feature=np.array(feature)
label=[0 ,1, 0, 0, 1]
index=0
calcInfoGain(feature,label,index)