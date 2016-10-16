from django.shortcuts import render_to_response
from sub.models import subject

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

    output_list = []
    if 'target' and 'wave' in locals():
        pool = [ { 'lv2': str(ele.level2), 'lv3': str(ele.level3), 'question': str(ele.question), 'question_top': str(ele.question_top), 'wave': ele.wave.split(',')[int(wave)-1], 'pk': ele.pk } for ele in subject.objects.filter(level1=target) if len(ele.wave.split(',')[int(wave)-1]) > 0 ]
        for ele in pool:
            if ele['question'] == ele['question_top']:
                pool[pool.index(ele)]['sort'] = ele['question_top']
            else:
                pool[pool.index(ele)]['sort'] = ele['question_top'] + ele['question']
        output_list = sorted( pool, key= lambda x: str(x['sort']) )

    return render_to_response('waves.html',{
        'targets'    : waves_list,
        'waves'      : wave_list,
        'wave'       : request.session['wave'],
        'sel_target' : request.session['target'],
        'sel_wave'   : request.session['wave'],
        'output'     : output_list,
    })
