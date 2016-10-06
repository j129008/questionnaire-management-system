from django.shortcuts import render_to_response
from sub.models import subject

def search(request):
    if 'keyword' not in request.GET:
        return render_to_response('search.html', { 'result': '' })
    keyword = request.GET['keyword']
    pool = [ { 'lv2': str(ele.level2), 'lv3': str(ele.level3), 'question': str(ele.question), 'question_top': str(ele.question_top), 'wave': ele.wave.split(','), 'pk': ele.pk } for ele in subject.objects.filter(question__contains=keyword) ]
    for ele in pool:
        if ele['question'] == ele['question_top']:
            pool[pool.index(ele)]['sort'] = ele['question_top']
        else:
            pool[pool.index(ele)]['sort'] = ele['question_top'] + ele['question']
    output_list = sorted( pool, key= lambda x: str(x['sort']) )

    return render_to_response('search.html', {
        'waveCnt': [ 'w'+str(cnt) for cnt in range(1,10)],
        'output' : output_list
    })
