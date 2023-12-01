# import matplotlib.pyplot as plt
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
# # 创建数据
# x = np.linspace(-2, 2, 100)  # 定义 x 的取值范围
# y = np.linspace(-2, 2, 100)  # 定义 y 的取值范围
# x, y = np.meshgrid(x, y)
#
# # 计算函数值
# z = x * np.exp(2 * y)
#
# # 绘制三维图形
# fig = plt.figure(figsize=(10, 8))
# ax = fig.add_subplot(111, projection='3d')
#
# # 绘制函数曲面
# ax.plot_surface(x, y, z, alpha=0.8, cmap='viridis')
#
# # 指定的点
# points = [(1, 0), (2, -1)]
#
# for point in points:
#     px, py = point
#     pz = px * np.exp(2 * py)  # 计算给定点的 z 值
#
#     # 计算斜率（梯度）
#     gradient_x = np.exp(2 * py)
#     gradient_y = 2 * px * np.exp(2 * py)
#
#     # 定义切线的参数
#     t = np.linspace(px - 0.5, px + 0.5, 10)
#     tx, ty = np.meshgrid(t, t)
#     tz = pz + gradient_x * (tx - px) + gradient_y * (ty - py)
#
#     # 绘制切线
#     ax.plot_surface(tx, ty, tz, alpha=0.5, color='red')
#
# # 设置坐标轴标签
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Plot of z = x * e^(2y) with Tangent Lines')
#
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 火箭的主体部分
body_x = np.linspace(-1, 1, 50)
body_y = np.linspace(-1, 1, 50)
body_x, body_y = np.meshgrid(body_x, body_y)
body_z = np.sqrt(body_x**2 + body_y**2)

ax.plot_surface(body_x, body_y, body_z, color='gray')

# 火箭的火焰部分
flame_x = np.linspace(-0.5, 0.5, 50)
flame_y = np.linspace(-0.5, 0.5, 50)
flame_x, flame_y = np.meshgrid(flame_x, flame_y)
flame_z = np.sqrt(flame_x**2 + flame_y**2)

ax.plot_surface(flame_x, flame_y, flame_z, color='orange')

# 设置坐标轴范围
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 2)

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
