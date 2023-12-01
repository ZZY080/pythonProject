import numpy as np
import matplotlib.pyplot as plt

# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 创建AM信号
f_carrier = 1000  # 载波频率
f_modulation = 10  # 调制信号频率
amplitude_modulation = 0.5  # 调制信号幅度
t = np.linspace(0, 1, 1000)  # 时间范围

carrier_signal = np.cos(2 * np.pi * f_carrier * t)  # 载波信号
modulation_signal = amplitude_modulation * np.cos(2 * np.pi * f_modulation * t)  # 调制信号

# 创建AM调制信号
am_signal = (1 + modulation_signal) * carrier_signal

# 解调AM信号
demodulated_signal = am_signal / carrier_signal

# 绘制原始AM信号和解调信号
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal)
plt.title("原始载波信号")

plt.subplot(3, 1, 2)
plt.plot(t, modulation_signal)
plt.title("调制信号")

plt.subplot(3, 1, 3)
plt.plot(t, demodulated_signal)
plt.title("解调信号")

plt.tight_layout()
plt.show()
