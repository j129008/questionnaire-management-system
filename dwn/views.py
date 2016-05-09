from django.shortcuts import render
from django.http import HttpResponse

def dwn(request):
    return HttpResponse("Hello World!")
