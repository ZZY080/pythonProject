from sklearn.ensemble import  RandomForestClassifier

def digit_predict(train_image,train_label,test_image):
    # n_estimators ：森林中决策树的数量；
    # criterion ：构建决策树时，划分节点时用到的指标。有 gini （基尼系数）, entropy (信息熵)。若不设置，默认为 gini；
    # max_depth ：决策树的最大深度，如果发现模型已经出现过拟合，可以尝试将该参数调小。若不设置，默认为 None；
    # max_features ：随机选取特征时选取特征的数量，一般传入 auto 或者 log2，默认为 auto ， auto 表示 max_features=sqrt(训练集中特征的数量) ；log2 表示 max_features=log2(训练集中特征的数量)。
    model=RandomForestClassifier(n_estimators=18)
    model.fit(train_image,train_label)
    result=model.predict(test_image)
    return result

