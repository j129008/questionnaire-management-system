import csv
from pprint import pprint
from glob import glob
import sys

if len(sys.argv) < 2:
    print("Usage: ./mergeCsvByID.py [folder name]")
    sys.exit()

fileList = glob(sys.argv[1]+'/*.csv*')

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
                data[row['id2']][key] = row[key]
            except:
                data[row['id2']] = dict()
                data[row['id2']][key] = row[key]
    f.close()

f = open('./merge.csv', 'w')
w = csv.writer(f, lineterminator='\n')

keyList.remove('id2')
keyList = ['id2'] + keyList
out = [keyList]

for id2 in data:
    line = [id2]
    for ele in keyList[1:]:
        try:
            line.append(data[id2][ele])
        except:
            line.append('')
    out.append(line)

w.writerows(out)
