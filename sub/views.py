from django.shortcuts import render_to_response
from .models import subject

subject_list = {'同儕關係': {'偏差行為': ['班級同學', '朋友', '自己本身', '家人', '校園'],
          '友誼網絡': ['班級同學', '朋友', '補習班同學'],
          '家庭間往來': [''],
          '溝通語言': [''],
          '班級人數': [''],
          '異性朋友': ['男女朋友'],
          '社會價值認同': [''],
          '職業選擇': ['班級同學', '朋友'],
          '親密程度': ['班級同學', '朋友'],
          '課業壓力比較': ['']},
 '學校生活': {'學校氣氛': [''],
          '學業表現': ['智育', '', '特殊才能', '課外活動表現', '擔任幹部'],
          '學生評價': ['對老師', '對同學', '對課程', '對學校', '班級氣氛', '班級成績比較'],
          '家長參與': ['熱衷程度', '學生家長導師互動', '父母要求學校及老師', '家長會', '義務工作與贊助'],
          '導師': ['基本資料',
                 '成長背景',
                 '憂鬱量表',
                 '婚姻狀況',
                 '家庭結構',
                 '教學經驗',
                 '進修情形',
                 '班級經營',
                 '教育理念',
                 '對體罰的態度',
                 '工作壓力源',
                 '工作成就感',
                 '教改現況及批評',
                 '對九年一貫看法'],
          '師生關係': ['師生互動', '師生相互喜惡'],
          '支持體系': [''],
          '校園偏差行為': [''],
          '男女合班合校': [''],
          '親師溝通': [''],
          '飲食與交通': ['']},
 '學生': {'升學經驗': ['升學方式', '升學壓力', '升學落點', '就學就業現況', '升學期望'],
        '基本資料': ['性別', '身心狀況', '生活作息', '宗教'],
        '就業經驗': ['職業期望'],
        '心理問題': ['憂鬱量表'],
        '態度、價值觀': ['性別角色',
                   '性別分工',
                   '道德觀',
                   '家庭價值',
                   '傳統家庭價值',
                   '孝道概念',
                   '社會讚許',
                   '社會公平觀',
                   '社會價值認同',
                   '反社會行為傾向'],
        '未來規劃': [''],
        '消費流行': ['零用金', '休閒活動', '他人認同', '品牌認同', '偶像認同'],
        '生活經驗': ['生活事件',
                 '補習經驗',
                 '打工',
                 '資訊網絡與傳播媒體',
                 '手機使用',
                 '旅遊經驗',
                 '第二性徵',
                 '性經驗'],
        '自我': ['自我概念', '自我評價', '自我效能', '自尊', '個人性格﹙內向、外向﹚'],
        '行為問題': ['偏差行為', '藥物濫用', '暴力及攻擊行為']},
 '家庭': {'代間關係': ['隔代關係', '父母與祖父母相互支持體系'],
        '家庭背景': ['家庭結構',
                 '家庭經濟',
                 '家庭凝聚性',
                 '家庭氣氛',
                 '婚姻關係',
                 '家庭暴力',
                 '教養看顧情形',
                 '家人偏差行為'],
        '家長參與學校活動': [''],
        '手足親戚': ['成績比較'],
        '教養態度': [''],
        '教養行為': ['正面教養', '不當教養'],
        '親子關係': ['家事參與', '親子互動', '學生獨立性', '親子溝通', '因升學的家庭改變']},
 '文化資本': {'社會贊許': ['']},
 '父母': {'中年危機': [''],
        '基本資料': ['身心狀況', '生活作息', '婚姻狀況'],
        '心理問題': ['憂鬱量表'],
        '態度、價值觀': ['性別角色',
                   '性別分工',
                   '道德觀',
                   '家庭價值',
                   '傳統家庭價值',
                   '孝道概念',
                   '社會讚許',
                   '社會公平觀'],
        '成長經驗(上一代家庭背景)': ['成長經驗(上一代家庭背景)', '家庭結構', '家庭經濟', '祖父母婚姻關係', '親子關係'],
        '生活經驗': ['生活事件'],
        '自我': ['自我概念', '自我評價', '自我效能', '自尊', '個人性格﹙內向、外向﹚'],
        '行為問題': ['偏差行為', '藥物濫用', '暴力及攻擊行為']},
 '研究方法': {'社會贊許': ['']},
 '社區': {'搬家經驗': [''],
        '現住社區評價': [''],
        '環境與治安': [''],
        '社區依附': [''],
        '社區參與': [''],
        '社區網絡與互動': ['']},
 '社會資本': {'社會贊許': ['']}}


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
        output_list = [ str(ele) for ele in subject.objects.filter(level1=request.session['level1'], level2=request.session['level2'], level3=request.session['level3']) ]

    if not 'saved' in request.session or not request.session['saved']:
        request.session['saved'] = []
        for ele in output_list:
            request.session['saved'].append([request.session['level1'], request.session['level2'], request.session['level3'], ele])
    else:
        for ele in output_list:
            request.session['saved'].append([request.session['level1'], request.session['level2'], request.session['level3'], ele])

    return render_to_response('subject.html', {
        'level1_list': subject_list,
        'level2_list': level2_list,
        'level3_list': level3_list,
        'selected1': request.session['level1'],
        'selected2': request.session['level2'],
        'selected3': request.session['level3'],
        'output': output_list,
        })
