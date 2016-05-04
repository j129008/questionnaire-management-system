from django.shortcuts import render_to_response
from django.http import HttpResponse
# from .models import subject

subject_list = {
    '學生':{
        '基本資料': ['性別', '宗教'],
        '生活經驗': ['生活事件']
    },
    '父母':{
        '成長經驗': ['祖父母背景']
    },
    '家庭':{},
    '同儕關係':{},
    '學校生活':{},
    '社區':{},
    '研究方法':{},
    '社會資本':{},
    '文化資本':{}
}



def sub(request):
    try:
        level2_list = subject_list[request.GET['level1']]
    except:
        level2_list = ''

    try:
        level3_list = subject_list[request.GET['level1']][request.GET['level2']]
    except:
        level3_list = ''

    try:
        selected1 = request.GET['level1']
    except:
        selected1 = ''

    try:
        selected2 = request.GET['level2']
    except:
        selected2 = ''

    try:
        selected3 = request.GET['level3']
    except:
        selected3 = ''

    return render_to_response('subject.html', {
        'level1_list': subject_list,
        'level2_list': level2_list,
        'level3_list': level3_list,
        'selected1': selected1,
        'selected2': selected2,
        'selected3': selected3,
        })
