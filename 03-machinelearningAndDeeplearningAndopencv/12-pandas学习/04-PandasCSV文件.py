import pandas as pd
# csv comma-separated values
df = pd.read_csv('data.csv')
# to_string() 用于返回 DataFrame 类型的数据，如果不使用该函数，则输出结果为数据的前面 5 行和末尾 5 行，中间部分以 ... 代替。
print(df)
print(df.to_string())


# 我们也可以使用 to_csv() 方法将 DataFrame 存储为 csv 文件：
name=['google','runoob','taobao','wiki']
site=['www.google.com','www.runoob.com','www.taobao.com','www.wiki.com']
age=[90,40,80,98]

dic={'name':name,'site':site,'age':age}

df2=pd.DataFrame(dic)
print(df2)
df2.to_csv("site.csv")

# 实例 - 读取前面 5 行
df3=pd.read_csv('./data.csv')
print(df3.head())
# 实例 - 读取前面 10 行
print(df3.head(10))
# 实例 - 读取末尾 5 行
print(df3.tail())
# 实例 - 读取末尾 10 行
print(df3.tail(10))
# info() 方法返回表格的一些基本信息：
print(df3.info())