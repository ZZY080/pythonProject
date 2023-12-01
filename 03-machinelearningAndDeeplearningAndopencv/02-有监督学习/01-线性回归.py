from sklearn.linear_model import  LinearRegression
from sklearn.metrics import  accuracy_score
import  matplotlib.pyplot as plt
X=[[10.0],[8.0],[13.0],[9.0],[11.0],[14.0],[6.0],[4.0],[12.0],[7.0],[5.0]]
y=[8.04,6.95,7.58,8.81,8.33,9.96,7.24,4.26,10.84,4.82,5.68]

model=LinearRegression()
model.fit(X,y)
y_pred=model.predict(X)
# print(y_pred)
# print(accuracy_score(y,y_pred))

plt.scatter(X,y)
plt.show()
