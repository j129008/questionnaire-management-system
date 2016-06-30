from xlrd import open_workbook
book = open_workbook('./J1data.xls')
first_sheet = book.sheet_by_index(0)


data = []
level1 = ''
level2 = ''
level3 = ''
for rrange in range(first_sheet.nrows):
    line = []
    for ele in first_sheet.row(rrange):
        cell = ele.value.strip()
        cell = cell.replace(',', '，').replace('\n','')
        line.append(cell)
    if len(line[0])>0:
        level1 = line[0]
    if len(line[1])>0:
        level2 = line[1]
    if len(line[2])>0:
        level3 = line[2]
    out = ''
    for ele in (['J1'+level1, level2, level3] + line[3:]):
        out+=ele+','
    print(out[:-1])
