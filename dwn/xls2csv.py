from xlrd import open_workbook
from glob import glob
import csv

fileList = glob('J1student/*.xlsx')

for fileName in fileList:
    print(fileName)
    out = []
    book = open_workbook(fileName)
    first_sheet = book.sheet_by_index(0)
    f = open(fileName.split('.')[0]+'.csv', 'w')
    w = csv.writer(f)

    for rrange in range(first_sheet.nrows):
        line = []
        for ele in first_sheet.row(rrange):
            try:
                cell = int(ele.value)
            except:
                cell = ele.value
            line.append(cell)
        out.append(line)
    #  out = zip(*out)
    w.writerows(out)
    f.close()
