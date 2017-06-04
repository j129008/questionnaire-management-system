from dwn.models import spss
#  from glob import glob

fp = open( './preproc/sum2.txt' ,'r')
for line in fp:
    spss.objects.create(question=line)
    print(line)
