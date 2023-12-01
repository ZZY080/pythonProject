import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 创建一个时间序列，表示一天的时间间隔
time = np.linspace(0, 24, 240)  # 假设每10分钟记录一次数据

# 模拟光合作用速率数据，这里使用简单的正弦函数作为示例
photosynthesis_rate = 10 * np.sin(2 * np.pi * time / 24) + 20

# 创建图表和坐标轴
fig, ax = plt.subplots()
ax.set_xlim(0, 24)
ax.set_ylim(0, 40)
line, = ax.plot([], [], lw=2)

# 更新函数，用于动态绘制曲线
def update(frame):
    line.set_data(time[:frame], photosynthesis_rate[:frame])
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(time), blit=True)

# 显示动画
plt.xlabel('时间 (小时)')
plt.ylabel('光合作用速率')
plt.title('植物一天的光合作用动态曲线图')
plt.show()
