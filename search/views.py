from django.shortcuts import render_to_response
from sub.models import subject

def search(request):
    if 'keyword' not in request.GET:
        return render_to_response('search.html', { 'result': '' })
    keyword = request.GET['keyword']

    return render_to_response('search.html', {
        'result' : keyword
    })
