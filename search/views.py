from django.shortcuts import render_to_response
from sub.models import subject

def search(request):
    if 'keyword' not in request.GET:
        return render_to_response('search.html', { 'result': '' })
    keyword = request.GET['keyword']
    pool = [ { 'question': str(ele.question), 'question_top': str(ele.question_top), 'wave': ele.wave.split(','), 'pk': ele.pk } for ele in subject.objects.filter(question__contains=keyword) ]

    return render_to_response('search.html', {
        'result' : pool
    })
