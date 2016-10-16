from django.shortcuts import render_to_response

def waves(request):
    return render_to_response('index.html')
