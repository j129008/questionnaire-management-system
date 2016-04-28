from django.shortcuts import render
from django.http import HttpResponse

def subject(request):
    return render(request, 'subject.html')
