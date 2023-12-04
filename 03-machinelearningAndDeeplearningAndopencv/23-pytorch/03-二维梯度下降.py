import torch
import matplotlib.pyplot as plt


# 定义函数 f(x) = x^2 + 2x + 1
def f(x):
    return x ** 2 + 2 * x + 1


# 定义函数的导数
def df(x):
    return 2 * x + 2


# 学习率
learning_rate = 0.1

# 初始化参数 x
x = torch.tensor([5.0], requires_grad=True)

# 存储历史数据用于可视化
x_history = [x.item()]
y_history = [f(x).item()]

# 迭代更新参数
for i in range(50):
    # 计算函数值
    y = f(x)

    # 反向传播求梯度
    y.backward()

    # 更新参数 x
    with torch.no_grad():
        x -= learning_rate * x.grad

    # 清空梯度
    x.grad.zero_()

    # 存储历史数据
    x_history.append(x.item())
    y_history.append(y.item())

# 可视化函数曲线和优化过程
x_vals = torch.linspace(-5, 3, 100)
plt.plot(x_vals.numpy(), f(x_vals).numpy(), label='f(x) = x^2 + 2x + 1')
plt.scatter(x_history, y_history, c='red', label='Gradient Descent')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent Optimization')
plt.legend()
plt.grid(True)
plt.show()
