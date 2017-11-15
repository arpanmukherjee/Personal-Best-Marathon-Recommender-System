

testList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/testData.txt')]
#testList = [line.rstrip('\n') for line in open('/home/shubhitiwari23/testData.txt')]
trainList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/trainData.txt')]

fileTrainM = open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/MaleTrainData.txt','w')
fileTrainF = open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/FemaleTrainData.txt','w')



for l in trainList:
    s = l.split('\t')
    if s[1] == 'M':
        fileTrainM.write(l+"\n")
    else:
        fileTrainF.write(l+"\n")

fileTrainM.close()
fileTrainF.close()

fileTestM = open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/MaleTestData.txt','w')
fileTestF = open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/FemaleTestData.txt','w')

for l in testList:
    s = l.split('\t')
    if s[1] == 'M':
        fileTestM.write(l + "\n")
    else:
        fileTestF.write(l+"\n")

fileTestM.close()
fileTestF.close()
