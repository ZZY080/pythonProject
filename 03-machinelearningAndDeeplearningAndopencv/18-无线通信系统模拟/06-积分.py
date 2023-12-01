# import numpy as np
# from scipy.integrate import quad
#
# # 定义被积函数
# def integrand(x):
#     return np.log(1 + a * x**2) * np.exp(-x**2)
#
# # 定义积分上下限
# a = 2.0  # 你可以根据需要设置a的值
# lower_limit = -np.inf
# upper_limit = np.inf
#
# # 使用quad函数进行积分
# result, error = quad(integrand, lower_limit, upper_limit)
#
# print("数值积分的近似结果:", result)
# print("积分误差:", error)

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 定义被积函数
def integrand(x, a):
    return np.log(1 + a * x**2) * np.exp(-x**2)

# 定义积分上下限
a = 2.0  # 设置a的值
x = np.linspace(-5, 5, 400)  # 生成x的值范围

# 计算函数值
y = integrand(x, a)

# 创建图形
plt.figure(figsize=(8, 6))
plt.plot(x, y, label=f'ln(1+{a}x^2)e^(-x^2)')
plt.title('被积函数图形')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# 显示图例
plt.legend()

# 显示图形
plt.show()

