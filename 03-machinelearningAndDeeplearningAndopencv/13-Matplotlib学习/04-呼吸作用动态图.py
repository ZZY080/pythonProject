import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 模拟呼吸速率参数
max_breathing_rate = 20.0  # 最大呼吸速率 (单位/s)

# 创建图表和坐标轴
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, max_breathing_rate)
line, = ax.plot([], [], marker='o', linestyle='-')

# 初始化时间和呼吸速率数据
time = np.linspace(0, 100, 1000)  # 时间序列
breathing_rate = np.zeros(len(time))

# 更新函数，用于动态绘制呼吸速率曲线
def update(frame):
    # 模拟呼吸速率的变化，这里使用正弦函数作为示例
    breathing_rate[frame] = max_breathing_rate * np.sin(2 * np.pi * frame / 100)

    # 更新曲线
    line.set_data(time[:frame+1], breathing_rate[:frame+1])
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(time), blit=True)

# 显示动画
plt.xlabel('时间 (单位)')
plt.ylabel('呼吸速率 (单位/s)')
plt.title('动态呼吸作用模拟')
plt.grid(True)
plt.show()
