import csv
from pprint import pprint
from glob import glob
fileList = glob('J1student/*.csv')

data = dict()
keyList = list()
for fileName in fileList:
    print(fileName)
    f = open(fileName, 'r')
    for row in csv.DictReader(f):
        for key in row.keys():
            if key not in keyList:
                keyList.append(key)
            try:
                data[row['id1']][key] = row[key]
            except:
                data[row['id1']] = dict()
                data[row['id1']][key] = row[key]
    f.close()

f = open('./merge.csv', 'w')
w = csv.writer(f, lineterminator='\n')

keyList.remove('id1')
keyList = ['id1'] + keyList
out = [keyList]

for id1 in data: 
    line = [id1]
    for ele in keyList[1:]:
        try:
            line.append(data[id1][ele])
        except:
            line.append('')
    out.append(line)

w.writerows(out)
