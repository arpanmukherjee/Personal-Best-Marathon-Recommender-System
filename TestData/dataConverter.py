def convert(data):
    temp = data.split('\t')
    t_time = int(float(temp[3]))
    temp[3] = str(t_time)
    t_temp = ""
    i = 0
    while i<len(temp)-1:
	t_temp += (str(temp[i])+"\t")
	i += 1
    t_temp += str(temp[i])
    return t_temp
	
	


f1 = open('trainData.txt', 'w')
f2 = open('testData.txt','w')
lines = [line.rstrip('\n') for line in open('updatedData.txt')]
per_dict = {}
for i in lines:
    temp = i.split('\t')
    if temp[3]=='-':
        continue
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
    for j in range(len(per_dict[key])-1):
        f1.write(convert(per_dict[key][j])+"\n")
    f2.write(convert(per_dict[key][j])+"\n");
f1.close()
f2.close()
