


sList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/finishers-boston-marathon-2015-2016-2017/inputTime')]
fileW = open("/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/finishers-boston-marathon-2015-2016-2017/outputTime",'w')
for temp in sList:
    s = temp.split(':')
    #print(s[0]+s[1])
    time = (int(s[0]) * 60) + int(s[1])
    fileW.write(str(time)+"\n")

fileW.close()
print(len(sList))