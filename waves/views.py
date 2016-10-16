from django.shortcuts import render_to_response

waves_list = {
    'J1學生': { 1, 2, 3, 4, 5, 6, 7, 8, 9 },
    'J3學生': { 1, 2, 3, 4, 5, 6, 7, 8 },
    'J1家長': { 1, 3, 6, 8, 9 },
    'J3家長': { 1, 4, 6, 7 }
}

def waves(request):
    return render_to_response('waves.html')
