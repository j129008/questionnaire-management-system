import pickle
from pprint import pprint
from sub.models import subject
from glob import glob


for dbName in glob('./tagList/*.pkl'):
    db = pickle.load(open(dbName,'rb'))

    for data in db:
        try:
            subject.objects.create(level1=data['v1'], level2=data['v2'], level3=data['v3'], question=data['question'], question_top=data['question_top'], wave=','.join(data['wave']))
        except:
            subject.objects.create(level1=data['v1'], level2=data['v2'], level3=data['v3'], question=data['question'], question_top='', wave=','.join(data['wave']))
