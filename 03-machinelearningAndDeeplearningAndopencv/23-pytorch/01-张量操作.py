import  torch

# 创建一个常量张量
x=torch.tensor([1,2,3,4,5])
print(x)

# 创建一个全为0的张量
zeros = torch.zeros(2,3)
print(zeros)
# 创建一个全为1的张量
ones=torch.ones(4,5)
print(ones)
# 张量加法
sum_tensor = x+ones
print(sum_tensor)

# 张量乘法
mul_tensor = x*2
print(mul_tensor)
# 张量矩阵乘法
matrix_a = torch.tensor([[1,2],[2,3]])
matrix_b=torch.tensor([[5,6],[7,8]])

matmul_twnsor = torch.matmul(matrix_a,matrix_b)
print(matmul_twnsor)