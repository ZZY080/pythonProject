import  torch

a= torch.randint(-10,10,(3,3),dtype=torch.int64)
print(a)

# 绝对值
b=torch.abs(a)
print(b)

# 加法处理
c = torch.add(a,b)
print(c)
d= torch.add(c,torch.tensor([10,10,10]))
print(d)
print("-"*100)
# 裁剪操作
e = torch.clamp(a,-7,9)
print(a)
print(e)
print("*"*100)
# 求商
f = torch.randint(1,10,(3,3),dtype=torch.int64)
print(a)
print(f)
g=torch.div(a,f)
print(g)
# 求幂操作 a的f次方
print(torch.pow(a,f))

"""
torch.mm：将参数传递到torch.mm后返回输入参数的求积结果作为输出，不过这个求积的方式和之前的torch.mul运算方式不太一样，
torch.mm运用矩阵之间的乘法规则进行计算，所以被传入的参数会被当作矩阵进行处理，参数的维度自然也要满足矩阵乘法的前提条件，
即前一个矩阵的行数必须和后一个矩阵列数相等
"""
print("*"*100)
h = torch.randint(1,3,(2,3),dtype=torch.int64)
i = torch.randint(1,3,(1,3),dtype=torch.int64)
# 矩阵乘法
j= torch.mm(h,i.T)
# 主元素相乘
k= torch.mul(h,i)
print(h)
print(i)
print(j)
print(k)

"""
将参数传递到torch.mv后返回输入参数的求积结果作为输出，torch.mv运用矩阵与向量之间的乘法规则进行计算，被传入的第1个参数代表矩阵，第2个参数代表向量，循序不能颠倒。
"""
print("*"*100)
l_1=torch.randint(1,3,(2,3),dtype=torch.int32)
l_2=torch.randint(1,3,(3,),dtype=torch.int32)
l_result = torch.mv(l_1,l_2)
print(l_1)
print(l_2)
print(l_result)
