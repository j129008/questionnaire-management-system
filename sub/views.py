from django.shortcuts import render_to_response
from .models import subject

subject_list = {'學生': {'代間關係': {'家事參與', '隔代關係', '親子互動', '教養行為', '親子溝通', '因升學的家庭改變', '學生獨立性'},
        '個人心理問題': {'憂鬱量表'},
        '個人行為問題': {'偏差行為', '暴力及攻擊行為', '藥物濫用'},
        '升學經驗': {'升學期望', '升學壓力', '就學現況', '升學落點', '升學方式'},
        '同儕偏差行為': {'校園偏差行為', '班級同學', '朋友'},
        '同儕社會價值認同': {'同儕社會價值認同'},
        '同儕關係／友誼網絡': {'補習班同學', '朋友', '親密程度', '班級同學', '異性朋友', '同學'},
        '問卷資料': {'問卷資料'},
        '基本資料': {'基本資料', '宗教', '生活作息', '身心狀況'},
        '學校生活': {'師生關係', '學校／班級狀況'},
        '學業表現': {'擔任幹部', '參與比賽', '特殊才能', '課外活動', '智育'},
        '學生評價': {'對同學', '班級氣氛', '對老師', '對課程', '對學校'},
        '家庭背景': {'父母婚姻狀況', '教養看顧情形', '家庭凝聚性', '家庭結構', '家庭氣氛', '居住狀況', '家庭經濟'},
        '就業經驗': {'就業現況', '職業期望'},
        '居住社區': {'社區評價', '搬家經驗', '居住環境', '社區參與'},
        '態度價值觀': {'家庭價值',
                  '對政治的看法',
                  '工作價值觀',
                  '性別分工',
                  '性別角色',
                  '社會價值認同',
                  '社會公平觀',
                  '社會讚許',
                  '道德觀'},
        '支持體系': {'支持體系'},
        '文化資本': {'文化資本'},
        '未來規劃': {'未來規劃'},
        '消費流行': {'偶像認同', '零用金及生活費', '他人認同', '品牌認同', '休閒活動'},
        '生活經驗': {'性經驗',
                 '手機使用',
                 '打工',
                 '旅遊經驗',
                 '生活事件',
                 '第二性徵',
                 '補習經驗',
                 '資訊網絡與傳播媒體'},
        '自我': {'個人性格', '自我評價', '自我概念'},
        '飲食與交通': {'飲食與交通'}}}


def sub(request):
    try:
        level2_list = subject_list[request.GET['level1']]
        request.session['level1'] = request.GET['level1']
    except:
        level2_list = ''
        request.session['level1'] = ''

    try:
        level3_list = subject_list[request.GET['level1']][request.GET['level2']]
        request.session['level2'] = request.GET['level2']
    except:
        level3_list = ''
        request.session['level2'] = ''


    try:
        request.session['level3'] = request.GET['level3']
    except:
        request.session['level3'] = ''

    output_list = []
    if (len(request.session['level1']) > 0 and len(request.session['level2']) >0 and len(request.session['level3']) >0):
        pool = [ { 'question': str(ele.question), 'question_top': str(ele.question_top), 'wave': ele.wave.split(','), 'pk': ele.pk } for ele in subject.objects.filter(level1=request.session['level1'], level2=request.session['level2'], level3=request.session['level3']) ]
        output_list = sorted( pool, key= lambda x: str(x['question_top'])+str(x['question']))
    if not 'saved' in request.session or not request.session['saved']:
        request.session['saved'] = []
        try:
            for ele in request.GET.getlist('question'):
                request.session['saved'].append([request.session['level1'], request.session['level2'], request.session['level3'], ele])
        except:
            pass
    else:
        try:
            for ele in request.GET.getlist('question'):
                request.session['saved'].append([request.session['level1'], request.session['level2'], request.session['level3'], ele])
        except:
            pass

    return render_to_response('subject.html', {
        'level1_list': subject_list,
        'level2_list': level2_list,
        'level3_list': level3_list,
        'selected1': request.session['level1'],
        'selected2': request.session['level2'],
        'selected3': request.session['level3'],
        'output': output_list,
        'waveCnt': [ 'w'+str(cnt) for cnt in range(1,10)],
        })
