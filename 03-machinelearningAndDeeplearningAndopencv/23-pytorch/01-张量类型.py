import  torch
a=torch.Tensor(2,2)
print(a)
b=torch.DoubleTensor(2,2)
print(b)
c=torch.Tensor([[1,2],[3,4]])
print(c)
d=torch.zeros(2,2)
print(d)
e=torch.ones(2,2)
print(e)
# 对角张量 默认为单位矩阵
f=torch.eye(2,2)
# 创建自己的对角矩阵
custom_elements = torch.tensor([2,3])
g=torch.diag_embed(custom_elements)
print(g)
# 随机张量
h=torch.rand(2,2)
print(h)
# 随机排列张量
i=torch.randperm(4)
print(i)
# 创建一个复数
real = torch.tensor(3.0)
imaginary = torch.tensor(2.0)
# 构建复数
complex_num = torch.complex(real,imaginary)
# 创建其共轭复数
conjugate_num = torch.conj(complex_num)
print(conjugate_num)
# 创建范围内的张量
k = torch.range(1,20,2)
print(k)

# 创建随机整数类型张量
l=torch.randint(low=0,high=10,size=(2,3),dtype=torch.int64)
print(l)
# 生成指定范围的随机小数
random_floats = (100)*torch.rand(2,3)+10
print(random_floats)