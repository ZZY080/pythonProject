import numpy as np
from sklearn.preprocessing import  PolynomialFeatures
from sklearn.linear_model import  Ridge
from sklearn.metrics import  mean_squared_error
train_size=20
test_size=12
train_x=np.random.uniform(low=0,high=1.2,size=train_size)
test_x=np.random.uniform(low=0.1,high=1.3,size=test_size)
train_y=np.sin(train_x*2*np.pi)+np.random.normal(0,0.2,train_size)
test_y=np.sin(test_x*2*np.pi)+np.random.normal(0,0.2,test_size)
poly=PolynomialFeatures(6)
train_poly_x=poly.fit_transform(train_x.reshape(train_size,1))
test_poly_x=poly.fit_transform(test_x.reshape(test_size,1))
model=Ridge()
model.fit(train_poly_x,train_y)
train_pred_y=model.predict(train_poly_x)
test_pred_y=model.predict(test_poly_x)
print(mean_squared_error(train_pred_y,train_y))
print(mean_squared_error(test_pred_y,test_y))