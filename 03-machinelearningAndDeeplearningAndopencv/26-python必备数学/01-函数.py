# import matplotlib.pyplot as plt
# import numpy as np
#
# # 定义 x 的取值范围
# x1 = np.linspace(0, 4, 100)  # 0 到 4 的范围
# x2 = np.linspace(-4, 0, 100)  # -4 到 0 的范围
#
# # 计算函数值
# y1 = np.sqrt(x1)  # 根号x
# y2 = -x2  # -x
#
# # 绘制图形
# plt.figure(figsize=(8, 6))
#
# plt.plot(x1, y1, label='sqrt(x)', color='blue')  # 根号x
# plt.plot(x2, y2, label='-x', color='red')  # -x
#
# plt.xlabel('x')
# plt.ylabel('f(x)')
# plt.title('Plot of sqrt(x) and -x')
#
# plt.axhline(0, color='black',linewidth=0.5)  # 绘制x轴
# plt.axvline(0, color='black',linewidth=0.5)  # 绘制y轴
#
# plt.legend()  # 显示图例
# plt.grid(True)  # 添加网格线
# plt.show()



# import matplotlib.pyplot as plt
# import numpy as np
#
# # 定义时间范围
# t = np.linspace(0, 10, 100)  # 时间范围从0到10，分100个点
#
# # 定义重力加速度
# g = 9.81  # 假设重力加速度为9.81 m/s^2
#
# # 计算函数值
# y = 0.5 * g * t**2  # 计算1/2 * g * t^2
#
# # 绘制图形
# plt.figure(figsize=(8, 6))
#
# plt.plot(t, y, label='1/2 * g * t^2', color='green')  # 1/2 * g * t^2
#
# plt.xlabel('Time (s)')
# plt.ylabel('Height (m)')
# plt.title('Plot of 1/2 * g * t^2')
#
# plt.axhline(0, color='black', linewidth=0.5)  # 绘制x轴
# plt.axvline(0, color='black', linewidth=0.5)  # 绘制y轴
#
# plt.legend()  # 显示图例
# plt.grid(True)  # 添加网格线
# plt.show()


