import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

trainData = [line.rstrip('\n') for line in open('TestData/trainDataWithSec.txt')]
testData = [line.rstrip('\n') for line in open('TestData/testDataWithSec.txt')]
trainDict = {}
testDict = {}

for i in trainData:
    item = i.split('\t')
    if item[0] in trainDict.keys():
        trainDict[item[0]].append(int(item[3]))
    else:
        tempList = []
        tempList.append(int(item[3]))
        trainDict[item[0]] = tempList

for i in testData:
    item = i.split('\t')
    testDict[item[0]] = int(item[3])


train_X = []
train_Y = []
test_X = []
test_Y = []

ind1 = ind = 0
for user in trainDict.keys():
    for i in range(len(trainDict[user])-1):
        train_X.append(trainDict[user][i])
        train_Y.append(trainDict[user][i+1])
        ind += 1
    test_X.append(trainDict[user][i])
    test_Y.append(testDict[user])
    ind1 += 1

train_X = np.asarray(train_X).reshape(-1, 1)
train_Y = np.asarray(train_Y).reshape(-1, 1)
test_X = np.asarray(test_X).reshape(-1, 1)
test_Y = np.asarray(test_Y).reshape(-1, 1)

model = LinearRegression()
model.fit(train_X, train_Y)
print model.score(test_X, test_Y)
plt.scatter(test_X, test_Y)
# plt.plot(test_Y, model.predict(test_X))
plt.show()
