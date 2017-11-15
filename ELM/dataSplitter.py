

sList = [line.rstrip('\n') for line in open('/media/adalove/WorkDrive/M.Tech/Sem 1/CF/MovieLens/ml-100k/u5.base')]
fileTrain = open("/media/adalove/WorkDrive/M.Tech/Sem 1/CF/MovieLens/ml-100k/output/u5.predicted",'w')
fileTest = open("/media/adalove/WorkDrive/M.Tech/Sem 1/CF/MovieLens/ml-100k/output/u5.predicted",'w')

i=0;

for temp in sList:
    p=temp.split('\t')
    if i==0:
        pre = p[0]
        for val in p:
            fileTrain.write(str(val)+"\t")
        t = []
        t.append(p)
    else:
        if pre==p[0]:
            t.append(p)
        else:
            //sdkfnks
