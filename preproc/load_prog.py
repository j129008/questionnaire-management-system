from dwn.models import program
from glob import glob

for fileName in glob('./program/*.txt'):
    fp = open(fileName,'r')
    for line in fp:
        program.objects.create(question=line)
