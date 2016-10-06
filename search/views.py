from django.shortcuts import render_to_response

# Create your views here.

def search(request):
    return render_to_response('search.html')
