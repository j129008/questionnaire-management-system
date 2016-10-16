from django.shortcuts import render_to_response

waves_list = {
    'J1學生': { 1, 2, 3, 4, 5, 6, 7, 8, 9 },
    'J3學生': { 1, 2, 3, 4, 5, 6, 7, 8 },
    'J1家長': { 1, 3, 6, 8, 9 },
    'J3家長': { 1, 4, 6, 7 }
}

def waves(request):
    wave_list = {}
    if 'target' not in request.session:
        request.session['target'] = ''

    if 'wave' not in request.session:
        request.session['wave'] = ''

    if 'target' in request.GET:
        target = request.GET['target']
        if len(target) > 1:
            wave_list = waves_list[target]
            request.session['target'] = target

    if 'wave' in request.GET:
        wave = request.GET['wave']
        if len(wave) > 0:
            request.session['wave'] = wave

    return render_to_response('waves.html',{
        'targets'    : waves_list,
        'waves'      : wave_list,
        'sel_target' : request.session['target'],
        'sel_wave'   : request.session['wave']
    })
