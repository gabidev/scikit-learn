import pandas as pd
from sklearn import svm, metrics

inputData = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

xor_df = pd.DataFrame(inputData)
trainingData = xor_df.ix[:, 0:1]
label = xor_df.ix[:, 2]

clf = svm.SVC()
clf.fit(trainingData, label)
pre = clf.predict(trainingData)

accuracy = metrics.accuracy_score(label, pre)
print("정확도: ", accuracy)