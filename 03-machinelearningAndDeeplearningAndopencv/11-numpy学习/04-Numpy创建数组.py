import  numpy as np


a=np.empty([3,2],dtype=int)
print(a)

# 默认位浮点数
b=np.zeros(5)
print(b)

# 设置数据类型
c=np.zeros((5,),dtype=int)
print(c)
# 自定义类型
d=np.zeros((2,2),dtype=[("x","i4"),("y","i4")])
print(d)

# 默认类型为float
e=np.ones(5)
print(e)
f=np.ones([2,2],dtype=int)
print(f)


f=np.array([[1,2,3],[4,5,6],[7,8,9]])
# 创建一个与 arr 形状相同的 所有元素都为0的数组
zeros_arr = np.zeros_like(f)
print(zeros_arr)

g=np.array([[1,2,3],[4,5,6],[7,8,9]])
# 创建一个与 arr 形状相同的 所有元素都为1的数组
ones_arr=np.ones_like(g)
print(ones_arr)

