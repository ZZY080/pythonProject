from sklearn.naive_bayes import MultinomialNB

# 生成数据
X_train=[
    [1,1,0,0,0,1,0,0,0,0,0],
    [0,1,1,1,0,0,0,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,0,0],
    [0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0],
    [0,0,0,0,0,1,1,1,0,0,1],
]
y_train=[1,1,1,0,0,0]
model=MultinomialNB()
model.fit(X_train,y_train)
pred=model.predict([[0,0,0,0,0,0,0,0,0,0,0]])
print(pred)