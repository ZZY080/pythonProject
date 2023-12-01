import numpy as np

# 一维
a= np.array([1,2,3])
print(a)
print(a[::-1])

# 二维
b= np.array([[1,2],[3,4]])
print(b)
print(b[::-1])

# 最小维度 转成二维
c= np.array([1,2,3],ndmin=2)
print(c)

# dtype参数
d=np.array([1,2,3],dtype=complex)
print(d)
