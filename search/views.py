from django.shortcuts import render_to_response
from sub.models import subject

def search(request):
    if 'keyword' not in request.GET:
        return render_to_response('search.html', {
            'keyword' : ''
        })
    if not 'saved' in request.session or not request.session['saved']:
        request.session['saved'] = []
        try:
            for ele in request.GET.getlist('question'):
                item = subject.objects.get(pk = ele.split('_')[0])
                request.session['saved'].append([item.level1, item.level2, item.level3, ele])
        except:
            pass
    else:
        try:
            for ele in request.GET.getlist('question'):
                item = subject.objects.get(pk = ele.split('_')[0])
                request.session['saved'].append([item.level1, item.level2, item.level3, ele])
        except:
            pass
    keyword = request.GET['keyword']
    setPool = [ ele.question_top for ele in subject.objects.filter(question__contains=keyword) ]
    setPool = list(set(setPool))
    setPool.remove('')
    pool = []
    for top in setPool:
        pool += [ { 'lv2': str(ele.level2), 'lv3': str(ele.level3), 'question': str(ele.question).replace(keyword, '<strong>'+keyword+'</strong>'), 'question_top': str(ele.question_top).replace(keyword, '<strong>'+keyword+'</strong>'), 'wave': ele.wave.split(','), 'pk': ele.pk } for ele in subject.objects.filter(question_top=top) ]
    pool += [ { 'lv2': str(ele.level2), 'lv3': str(ele.level3), 'question': str(ele.question).replace(keyword, '<strong>'+keyword+'</strong>'), 'question_top': str(ele.question_top).replace(keyword, '<strong>'+keyword+'</strong>'), 'wave': ele.wave.split(','), 'pk': ele.pk } for ele in subject.objects.filter(question_top='', question__contains=keyword) ]
    for ele in pool:
        if ele['question'] == ele['question_top']:
            pool[pool.index(ele)]['sort'] = ele['question_top']
        else:
            pool[pool.index(ele)]['sort'] = ele['question_top'] + ele['question']
    output_list = sorted( pool, key= lambda x: str(x['sort']) )

    return render_to_response('search.html', {
        'waveCnt': [ 'w'+str(cnt) for cnt in range(1,10)],
        'output' : output_list,
        'keyword' : keyword
    })
