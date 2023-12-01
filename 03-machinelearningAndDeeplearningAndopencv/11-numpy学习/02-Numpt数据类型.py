import numpy as np

# 使用标量类型
a=np.dtype(np.int32)
print(a)

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
b=np.dtype("int8")
print(b)
# 字节顺序标注
c=np.dtype("<i4")
print(c)
# 首先创建结构化数据类型
d=np.dtype([("age",np.int8)])
print(d)
# 将数据类型应用于 ndarray 对象
e=np.dtype([('age',np.int8)])
f=np.array([(10,),(20,),(30,)],dtype=e)
print(f)
print(f["age"])

# 实际应用
g=np.dtype([("name","S20"),("age","i1"),("marks","f4")])
print(g)

h= np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
i= np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = h)
print(i)