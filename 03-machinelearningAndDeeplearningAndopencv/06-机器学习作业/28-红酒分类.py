from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
def classification(train_feature,train_label,test_feature):
    scaler=StandardScaler()
    train_feature=scaler.fit_transform(train_feature)
    test_feature=scaler.transform(test_feature)
    model=KNeighborsClassifier(n_neighbors=10)
    model.fit(train_feature,train_label)
    return model.predict(test_feature)

data=load_wine()
X_train,X_test,y_train,y_test=train_test_split(data.data,data.target,train_size=0.8)
print(classification(X_train,y_train,X_test))
