import pandas as pd
import  numpy as np
from sklearn.datasets import  load_breast_cancer
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import  accuracy_score
data=load_breast_cancer()
X=pd.DataFrame(data.data,columns=data.feature_names)
y=pd.DataFrame(data.target,columns=['result'])
df=pd.concat([X,y],axis=1)
target_colums=list(df.columns[:10])
X=df.loc[:,target_colums]

X=np.array(X)
y=np.array(y).flatten()

# 得到模型
model=LogisticRegression()
# 训练模型
model.fit(X,y)
# 模型预测
y_pred=model.predict(X)

# 模型评估
score=accuracy_score(y,y_pred)
print(score)


