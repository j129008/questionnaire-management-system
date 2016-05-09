from django.shortcuts import render_to_response

def dwn(request):
    return render_to_response('download.html')
