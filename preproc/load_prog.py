from dwn.models import program
#  from glob import glob

fp = open( './preproc/sum2.txt' ,'r')
for line in fp:
    program.objects.create(question=line)
    print(line)
