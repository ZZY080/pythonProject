from sklearn.datasets import  load_breast_cancer
from sklearn.linear_model import  LogisticRegression
from sklearn.metrics import  confusion_matrix,accuracy_score,precision_score,recall_score,f1_score
data=load_breast_cancer()
X=data.data
# 反转标签0和1
y=1-data.target
X=X[:,:10]
model_lor=LogisticRegression()
model_lor.fit(X,y)
y_pred=model_lor.predict(X)

# 混淆矩阵评估模型
cm=confusion_matrix(y,y_pred)
score=accuracy_score(y,y_pred)
pscore=precision_score(y,y_pred)
rscore=recall_score(y,y_pred)
fscore=f1_score(y,y_pred)
print(cm)
print(score)
print(pscore)
print(rscore)
print(fscore)


