import pandas as pd

a=[1,2,3]
myvar = pd.Series(a)
print(myvar)
print("------------")
print(myvar[0])
print("-------------------------")
# 我们可以指定索引值
b=['google','runnob','wiki']
c=pd.Series(b,index=["x","y","z"])
print(c)
print(c["x"])
print("-------------------------")
# 我们也可以使用 key/value 对象，类似字典来创建 Series：
d={1:"google",2:"runnob",3:"wiki"}
e=pd.Series(d)
print(e)
print(e[1])

# 设置 Series 名称参数：
f = {1: "Google", 2: "Runoob", 3: "Wiki"}

g= pd.Series(f, index = [1, 2], name="RUNOOB-Series-TEST" )

print(g)