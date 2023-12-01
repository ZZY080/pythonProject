import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 模拟光合作用参数
Vcmax = 40.0  # 最大羧化速率 (μmol/m2/s)
Jmax = 60.0   # 最大电子传递速率 (μmol/m2/s)
temperature = 25.0  # 温度 (摄氏度)

# 创建图表和坐标轴
fig, ax = plt.subplots()
ax.set_xlim(0, 1000)
ax.set_ylim(0, 50)
line, = ax.plot([], [], marker='o', linestyle='-')

# 初始化光照强度和光合作用速率
light_intensity = np.arange(0, 1001, 10)  # 光照强度范围
photosynthesis_rate = np.zeros(len(light_intensity))

# 更新函数，用于动态绘制曲线
def update(frame):
    # 更新光照强度和光合作用速率
    light = light_intensity[frame]
    photosynthesis = min(Vcmax * (light / (light + 2 * Jmax)), Vcmax * (1 - np.exp(-light / (2 * Vcmax))))
    photosynthesis_rate[frame] = photosynthesis

    # 更新曲线
    line.set_data(light_intensity[:frame+1], photosynthesis_rate[:frame+1])
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=len(light_intensity), blit=True)

# 显示动画
plt.xlabel('光照强度 (μmol/m2/s)')
plt.ylabel('光合作用速率 (μmol/m2/s)')
plt.title('动态光合作用模拟')
plt.grid(True)
plt.show()
