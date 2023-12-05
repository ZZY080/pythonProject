import numpy as np

# 定义函数 f(x, y)
def f(x, y):
    return x**2 + 2*y

# 定义函数 f 关于 x 和 y 的偏导数
def gradient_f(x, y):
    df_dx = 2*x  # f 关于 x 的偏导数
    df_dy = 2    # f 关于 y 的偏导数
    return np.array([df_dx, df_dy])

# 梯度下降算法
def gradient_descent(learning_rate, iterations):
    # 初始参数值
    params = np.array([0.0, 0.0])

    # 迭代更新参数
    for i in range(iterations):
        grad = gradient_f(params[0], params[1])  # 计算梯度
        params = params - learning_rate * grad  # 更新参数

        # 打印每次迭代后的结果
        print(f"Iteration {i+1}: params = {params}, f(params) = {f(params[0], params[1])}")

    return params

# 设置学习率和迭代次数
learning_rate = 0.1
iterations = 10

# 运行梯度下降算法
optimal_params = gradient_descent(learning_rate, iterations)
