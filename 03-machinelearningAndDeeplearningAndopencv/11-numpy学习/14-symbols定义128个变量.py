import  sympy as sp
import numpy as np

# 定义128个变量
variables = sp.symbols("x1:129")
variables=list(variables)

# 将符号变量列表转换为 Numpy 数组(行向量)
numpy_vector = np.array(variables)

# 为符号变量赋随机值
random_values = np.random.rand(len(numpy_vector))

for i in range(len(numpy_vector)):
    numpy_vector[i] = random_values[i]

print(numpy_vector)
print(numpy_vector[0])