import  numpy as np

# 以下实例获取数组中 (0,0)，(1,1) 和 (2,0) 位置处的元素。
a=np.array([[1,2],[3,4],[5,6]])
b=a[[0,1,2],[0,1,0]]
print(b)
print("------------------------------------------------")
# 以下实例获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]。
d=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(d)
rows=np.array([[0,0],[3,3]])
cols=np.array([[0,2],[0,2]])
e=d[rows,cols]
print(e)
print("-------------------------------------------------")
# 可以借助切片 : 或 … 与索引数组组合
f=np.array([[1,2,3],[4,5,6],[7,8,9]])
g=f[1:3,1:3]
h=f[1:3,[1,2]]
i=f[...,1:]
print(g)
print(h)
print(i)
print("----------------------------------------")

# 布尔索引
k=np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
print(k>5)
print(k[k>5])

# 以下实例使用了 ~（取补运算符）来过滤 NaN。
l=np.array([np.nan,1,2,np.nan,3,4,5])
print(a[~np.isnan(a)])

# 以下实例演示如何从数组中过滤掉非复数元素。
m=np.array([1,2+6j,5,3.5+5j])
print(m[np.iscomplex(m)])