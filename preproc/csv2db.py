fp = open('./data.csv','r')
data = []

for line in fp:
    data.append(line.strip().split(','))

col1=''
col2=''
col3=''
col4=''

db = []
for line in data:
    if len(line[0]) > 0:
        col1 = line[0].strip()
    if len(line[1]) > 0:
        col2 = line[1].strip()
    if len(line[2]) > 0:
        col3 = line[2].strip()
    if len(line[3]) > 0:
        col4 = line[3].strip()

    if len(col4)>0 and len(col3)>0:
        # print(col1+'|'+col2+'|'+col3+'|'+col4)
        db.append([col1,col2,col3,col4])
