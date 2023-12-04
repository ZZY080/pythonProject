import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义函数 f(x, y) = x^2 + y^2
def f(x, y):
    return x ** 2 + y ** 2


# 定义函数的偏导数
def df(x, y):
    return 2 * x, 2 * y


# 学习率
learning_rate = 0.1

# 初始化参数 x 和 y
x = torch.tensor([3.0], requires_grad=True)
y = torch.tensor([4.0], requires_grad=True)

# 存储历史数据用于可视化
x_history = [x.item()]
y_history = [y.item()]
z_history = [f(x, y).item()]

# 迭代更新参数
for i in range(50):
    # 计算函数值
    z = f(x, y)

    # 反向传播求梯度
    z.backward()

    # 更新参数 x 和 y
    with torch.no_grad():
        x -= learning_rate * x.grad
        y -= learning_rate * y.grad

    # 清空梯度
    x.grad.zero_()
    y.grad.zero_()

    # 存储历史数据
    x_history.append(x.item())
    y_history.append(y.item())
    z_history.append(z.item())

# 可视化优化过程
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 生成网格点坐标
x_vals = torch.linspace(-5, 5, 100)
y_vals = torch.linspace(-5, 5, 100)
x_grid, y_grid = torch.meshgrid(x_vals, y_vals)
z_grid = f(x_grid, y_grid)

# 绘制函数曲面
ax.plot_surface(x_grid.numpy(), y_grid.numpy(), z_grid.numpy(), cmap='viridis', alpha=0.5)

# 绘制优化过程的轨迹
ax.scatter(x_history, y_history, z_history, c='red')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('Gradient Descent Optimization in 3D')

plt.show()
