import  numpy as np

def train(filename):
    with open(filename,'r',encoding='utf8') as f:
        contentlist=f.readlines()
        if '\n' in contentlist:
            index=contentlist.index('\n')
            contentlist=contentlist[1:index]
            data_float=np.array(contentlist,dtype=float)
            result=np.mean(data_float)
    return result

file_path='./data/1.斗地主模拟结果1.txt'
result=train(file_path)
print(result)