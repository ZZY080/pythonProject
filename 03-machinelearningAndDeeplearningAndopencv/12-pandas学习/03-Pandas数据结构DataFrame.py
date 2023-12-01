import pandas as pd
import warnings



warnings.filterwarnings('ignore', category=FutureWarning)
data1=[["google",10],["runoob",12],['wiki',13]]
df1=pd.DataFrame(data1,columns=['site','age'],dtype=float)
print(df1)


data2={"site":["google","runoob","wiki"],"age":[10,12,13]}
df2=pd.DataFrame(data2)
print(df2)


data3=[{"a":1,"b":2},{"a":5,"b":10,"c":20}]
df3=pd.DataFrame(data3)
print(df3)


data4={
    "calories":[420,380,390],
    "duration":[50,40,45]
}

# 数据载入到DataFrame对象

df4=pd.DataFrame(data4)
print(df4.loc[0])
print(df4.loc[1])



