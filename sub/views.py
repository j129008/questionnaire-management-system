from django.shortcuts import render
from django.http import HttpResponse
from .models import Lv1

def subject(request):
    lv1_list = Lv1.objects.all()
    return render(request, 'subject.html', {
        'lv1_list': lv1_list,
        })
