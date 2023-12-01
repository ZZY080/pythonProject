import  matplotlib.pyplot as plt
import  numpy as np

# 解决中文问题
plt.rcParams['font.sans-serif']=['SimHei']

x1=np.linspace(-5,5,101)
y1=np.sin(x1)
# 简单操作
# plt.plot(x1,y1)
# plt.show()

# 严密操作
fig,ax=plt.subplots(nrows=2,ncols=2,figsize=(5,5))
ax[0][1].set_title("正弦函数")
ax[0][1].set_xlabel("横坐标")
ax[0][1].set_ylabel("正弦函数值")

ax[0][1].plot(x1,y1)

plt.show()