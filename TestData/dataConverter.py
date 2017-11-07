f1 = open('RaceDataFull','w')
lines = [line.rstrip('\n') for line in open('updatedData.txt')]
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
        temp = per_dict[key][j].split('\t')
        t_time = int(float(temp[3]))
        temp[3] = str(t_time)
        t_temp = ""
        i = 0
        while i<len(temp)-1:
            t_temp += (str(temp[i])+"\t")
            i += 1
        t_temp += str(temp[i])
        f1.write(str(t_temp)+'\n')
f1.close()
