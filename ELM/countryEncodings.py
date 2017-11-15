cList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/Project/Personal-Best-Marathon-Recommender-System/TestData/countryList.txt')]

enc = []
n = len(cList)
i=0
for line in cList:
    s = line.split('\n')
    print "'"+s[0]+"' : [",
    for k in range(n):
        if(k==i):
            print 1,
        else:
            print 0,
        if k == n-1:
            continue
        else:
            print ',',
    print "]",
    print ",",

    i = i+1
    print('\n')
