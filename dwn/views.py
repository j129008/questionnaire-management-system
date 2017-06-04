from django.shortcuts import render_to_response
from sub.models import subject
from dwn.models import program
from dwn.models import spss
from django.http import HttpResponse
import os
import csv
from glob import glob
from pprint import pformat

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
        if 'delete' in request.GET:
            delList = request.GET['delete'].split('_')
            for delTag in delList:
                request.session['saved'] = [ x for x in request.session['saved'] if delTag not in x[3] ]

        if 'downloadAll' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            response.write('\ufeff')
            f = open('dwn/merge.csv', 'r')
            outList = [ ele[3].split("-")[1].lower() for ele in request.session['saved'] ]
            outList = ['id2'] + outList
            writer.writerow(outList)
            for row in csv.DictReader(f):
                line = []
                for x in outList:
                    try:
                        line.append(row[x])
                    except:
                        line.append('')
                writer.writerow(line)
            f.close()
            return response
        if 'downloadProg' in request.GET:
            response = HttpResponse(content_type='text/txt')
            response['Content-Disposition'] = 'attachment; filename="program.txt"'
            outList = [ ele[3].split("-")[1] for ele in request.session['saved'] ]
            for keyword in outList:
                try:
                    response.write(keyword+':\r\n')
                    for s in program.objects.filter(question__contains=keyword):
                        response.write(str(s)+'\r\n')
                    response.write('\r\n')
                except Exception as e:
                    print( str(e) )
            return response
        if 'downloadList' in request.GET:
            response = HttpResponse(content_type='text/txt')
            response['Content-Disposition'] = 'attachment; filename="list.txt"'
            response.write(pformat(out).replace('\n','\r\n'))
            return response
        if 'downloadProg_SPSS' in request.GET:
            response = HttpResponse(content_type='text/txt')
            response['Content-Disposition'] = 'attachment; filename="program_SPSS.txt"'
            outList = [ ele[3].split("-")[1] for ele in request.session['saved'] ]
            for keyword in outList:
                try:
                    response.write(keyword+':\r\n')
                    for s in spss.objects.filter(question__contains=keyword):
                        response.write(str(s)+'\r\n')
                    response.write('\r\n')
                except Exception as e:
                    print( str(e) )
            return response
        if 'saved' not in request.session:
            request.session['saved'] = []

    except Exception as e:
        print(str(e))
    tags = {}
    data = {}
    global out
    out = []
    for rec in request.session['saved']:
        try:
            pk = rec[3].split('-')[0]
            tag = rec[3].split('-')[1]
        except:
            request.session['saved'] = []
            return render_to_response('download.html')
        try:
            tags[pk].append(tag)
        except:
            tags[pk] = []
            tags[pk].append(tag)
        try:
            ques = subject.objects.get(pk=pk).question
            ques_top = subject.objects.get(pk=pk).question_top
            tagList = subject.objects.get(pk=pk).wave
        except:
            request.session['saved'] = []
            return render_to_response('download.html')
        waveList = ''
        i = 0
        for w in tagList.split(','):
            i += 1
            if w != '':
                waveList += 'w'+str(i)+' '

        if ques != ques_top:
            data[pk] = [rec[0] ,waveList , rec[1] , rec[2] , ques_top+' '+ques , ", ".join(tags[pk])]
        else:
            data[pk] = [rec[0] ,waveList , rec[1] , rec[2] , ques                , ", ".join(tags[pk])]
    for key in data:
        out.append(data[key])

    return render_to_response('download.html',{
        'saved': out,
    })
