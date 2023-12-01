import numpy as np

a= np.arange(24)
print(a.ndim)
b=np.array([[1],[2]])
print(b.ndim)
print("---------------------------------------")
# 现调整其大小
c=a.reshape(2,4,3)
print(c)
print(c.ndim)
print("---------------------------------------")

d=np.array([[1,2,3],[4,5,6]])
print(d.shape)
d.shape=(3,2)
print(d)
print("---------------------------------------")

e=np.array([[1,2,3],[4,5,6]])
f=e.reshape(3,2)
print(f)
print("---------------------------------------")

g=np.array([1,2,3,4,5],dtype=np.int8)
print(g.itemsize)
h=np.array([1,2,3,4,5],dtype=np.float64)
print(h.itemsize)
print("---------------------------------------")

i=np.array([1,2,3,4,5])
print(i.flags)
