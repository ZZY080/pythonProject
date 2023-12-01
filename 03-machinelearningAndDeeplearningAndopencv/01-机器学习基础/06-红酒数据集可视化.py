from sklearn.datasets import  load_wine
import  matplotlib.pyplot as plt
data=load_wine()
x3=data.data[:,[0]]
y3=data.data[:,[9]]
plt.scatter(x3,y3)
plt.show()
