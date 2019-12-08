import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

irisData = load_iris()

X_train, X_test, y_train, y_test = train_test_split(irisData['data'], irisData['target'], random_state = 0)
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

y_predict = knn.predict(X_test)
print("정확도 np.mean 사용: ", np.mean(y_test == y_predict))
