import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

csv = pd.read_csv('iris.csv')

csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]

X_train, X_test, y_train, y_test = train_test_split(csv_data, csv_label)

clf = svm.SVC()
clf.fit(X_train, y_train)
y_predict = clf.predict(X_test)

ac_score = metrics.accuracy_score(y_test, y_predict)
print("정확도: ", ac_score)
