import numpy as np

a=np.arange(10)
b=slice(2,7,2)
print(a[b])

c=np.arange(10)
d=c[2:7:2]
print(d)

e=np.arange(10)
f=e[5]
print(f)

g=np.arange(10)
h=g[2:]
print(h)
i=g[2:5]
print(i)
print("-----------------------------------------------")
# 多维数组
j=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(j)
print(j[1:])
print("------------------------------------")
# 返回某列
k=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(k[...,0])
print(k[1,...])
print(k[...,1:])
