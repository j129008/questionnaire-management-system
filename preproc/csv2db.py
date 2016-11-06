import csv
import re
from pprint import pprint
import pickle
import sys

if len(sys.argv) < 2:
    print("Usage: ./csv2db.py [file name]")
    sys.exit()

for fname in sys.argv[1:]:
    fp = open(fname,'r')

    db = dict()
    for line in csv.reader(fp):
        for i in range(len(line)):
            line[i] = re.sub(r'',' ',line[i])
            line[i] = re.sub('\s+',' ',line[i])
            line[i] = re.sub('^[\d.]+','',line[i])
        if len(line[0]) > 1:
            col1 = line[0]
        if len(line[1]) > 1:
            col2 = line[1]
        if len(line[2]) > 1:
            col3 = line[2]
        if len(line[3]) > 1:
            col4 = line[3]

        if len(col4)>1 and len(col3)>1:
            if col1 not in db:
                db[col1] = dict()
            if col2 not in db[col1]:
                db[col1][col2] = dict()
            if col3 not in db[col1][col2]:
                db[col1][col2][col3] = list()
            if col4[0] == ' ':
                try:
                    db[col1][col2][col3][-1].append([col4.strip(), line[4:]])
                except:
                    db[col1][col2][col3].append([[col4.strip(), line[4:]]])
            else:
                db[col1][col2][col3].append([[col4.strip(), line[4:]]])

    db2 = dict()
    for v1 in db:
        for v2 in db[v1]:
            for v3 in db[v1][v2]:
                for ins in db[v1][v2][v3]:
                    save = dict()
                    save['v1'] = v1
                    save['v2'] = v2
                    save['v3'] = v3
                    if len(ins) > 1:
                        for ele in ins:
                            save['question'] = ele[0]
                            save['wave'] = ele[1]
                            save['question_top'] = ins[0][0]
                            db2[ins[0][0] + ele[0]] = save.copy()
                    else:
                        save['question'] = ins[0][0]
                        save['wave'] = ins[0][1]
                        db2[ins[0][0]] = save.copy()

    db3 = []
    for key in db2:
        db3.append(db2[key])
        ele = db2[key]
    pickle.dump(db3, open(fname+'.pkl', 'wb'))
    fp.close()
