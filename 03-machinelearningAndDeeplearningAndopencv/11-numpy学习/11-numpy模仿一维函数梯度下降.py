"""
下面是使用 NumPy 实现简单的梯度下降算法的示例。这个例子假设我们要最小化一个简单的函数 f(x)=x^2+5x+6

"""
import numpy as np

# 定义一个函数 f(x)=x^2+5x+6
def function(x):
    return x**2+5*x+6

# 计算函数 f(x) 关于x的导数
def gradient(x):
    return 2*x+5

# 梯度下降算法
def gradient_descent(learning_rate,iterations):
    # 初始参数值
    x=0
    # 迭代更新参数
    for i in range(iterations):
        grad = gradient(x) # 计算梯度
        x=x-learning_rate*grad
        # 打印每次迭代后的结果
        print(f"Iteration {i+1}:x={x},f(x)={function(x)}")
    return x

# 设置学习率和迭代次数
learning_rate = 0.001
iterations = 10000
# 运行梯度下降算法
optimal_x = gradient_descent(learning_rate,iterations)