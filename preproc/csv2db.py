import csv
import re
fp = open('./data.csv','r')

for line in csv.reader(fp):
    for i in range(len(line)):
        line[i] = re.sub(r'',' ',line[i])
        line[i] = re.sub('\s+',' ',line[i])
    if len(line[0]) > 0:
        col1 = line[0]
    if len(line[1]) > 0:
        col2 = line[1]
    if len(line[2]) > 0:
        col3 = line[2]
    if len(line[3]) > 0:
        col4 = line[3]

    if len(col4)>0 and len(col3)>0:
        print(col1+'|'+col2+'|'+col3+'|'+col4)
        #  db.append([col1,col2,col3,col4])
