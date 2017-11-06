f1 = open('updatedData.txt','w')
lines = [line.rstrip('\n') for line in open('RaceDataFull')]
per_dict = {}
for i in lines:
    temp = i.split('\t')
    try:
        if temp[0] in per_dict.keys():
            per_dict[temp[0]].append(i)
        else:
            race_time = []
            race_time.append(i)
            per_dict[temp[0]] = race_time
    except:
        print temp


for key in per_dict:
    if len(per_dict[key]) < 3:
        continue
    for j in range(len(per_dict[key])):
        f1.write(str(per_dict[key][j])+'\n')
f1.close()
