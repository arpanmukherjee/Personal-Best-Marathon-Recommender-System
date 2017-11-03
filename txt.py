f = open('output.txt','w')
f1 = open('no_of_races.txt','w')
lines = [line.rstrip('\n') for line in open('ip.txt')]
per_dict = {}
for i in lines:
    temp = i.split('\t')
    try:
        if temp[0] in per_dict.keys():
            per_dict[temp[0]].append(int(float(temp[3])))
        else:
            race_time = []
            race_time.append(int(float(temp[3])))
            per_dict[temp[0]] = race_time
        f.write(str(i)+'\n')
    except:
        print temp

ctr= []

for item in dict:
    ctr.append(len(per_dict[item]))
ctr.sort()
for i in ctr:
    f1.write(str(i)+'\n');
f1.close()
f.close()
