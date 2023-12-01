import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 光照强度数据
light_intensity = [100, 200, 300, 400, 500]
# 对应的光合速率数据
photosynthesis_rate = [10, 20, 30, 25, 15]

# 创建一个散点图
plt.scatter(light_intensity, photosynthesis_rate, label='光合速率', color='green', marker='o')
plt.xlabel('光照强度 (光照单位)')
plt.ylabel('光合速率 (单位/时间)')
plt.title('光照强度与光合速率关系')
plt.legend()
plt.grid(True)

# 显示图表
plt.show()
