testList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/testData.txt')]
trainList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/trainData.txt')]

country = set()
age =[]
time = []
for temp in trainList:
    p = temp.split('\t')
    age.append(int(p[2]))
    time.append(int(p[3]))
    country.add(p[4])


for temp in testList:
    p = temp.split('\t')
    age.append(int(p[2]))
    time.append(int(p[3]))
    country.add(p[4])


print("max age : "+str(max(age)))
print("min age : "+str(min(age)))
print("max time : "+str(max(time)))
print("min time : "+str(min(time)))
print("no of countries : "+ str(len(country)))


for k in country:
    print k




