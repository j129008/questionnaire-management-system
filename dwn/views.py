from django.shortcuts import render_to_response

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
    except:
        pass
    return render_to_response('download.html',{
        'saved': request.session['saved'],
    })
