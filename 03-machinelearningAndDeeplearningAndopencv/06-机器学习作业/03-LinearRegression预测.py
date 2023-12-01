import numpy as np
from sklearn.linear_model import  LinearRegression
def train(filename):
    with open(filename,'r',encoding='utf8') as f:
        contentlist=f.readlines()
        if '\n' in contentlist:
            index=contentlist.index('\n')
            contentlist=contentlist[1:index]
            data_list=np.array(contentlist,dtype=float)
            x=[i for i in range(1,len(data_list)+1)]
            x=np.array(x,dtype=float).reshape(-1,1)
            y=data_list
            model=LinearRegression()
            model.fit(x,y)
            y_pred=model.predict([[100]])
    return  y_pred[0]
file_path='./data/1.斗地主模拟结果1.txt'
result=train(file_path)
print(result)