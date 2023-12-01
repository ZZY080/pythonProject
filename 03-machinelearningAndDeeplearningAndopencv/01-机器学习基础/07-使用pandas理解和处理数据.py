import  pandas as pd
import  matplotlib.pyplot as plt
from sklearn.datasets import  load_wine
data=load_wine()
df_x=pd.DataFrame(data.data,columns=data.feature_names)
print(df_x.head())
df_y=pd.DataFrame(data.target,columns=['target'])
print(df_y.head())
df=pd.concat([df_x,df_y],axis=1)
print(df.loc[:,"alcohol"])
plt.hist(df.loc[:,"alcohol"])
plt.show()