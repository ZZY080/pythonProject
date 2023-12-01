from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
import  numpy as np

import  sklearn.metrics

pp=Pipeline([
    ('count',CountVectorizer()),
    ('mm',LinearSVC())
])
pp.fit(X_train,y_train)
predicted=pp.predict(X_test)
acc=np.mean(predicted==y_test)
print(acc)