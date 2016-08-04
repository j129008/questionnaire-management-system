from django.shortcuts import render_to_response
from sub.models import subject
from django.http import HttpResponse
import os
import csv

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
        if 'download' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            f = open('dwn/merge.csv', 'r')
            outList = ['id1'] + request.GET['download'].split('_')
            writer.writerow(outList)
            for row in csv.DictReader(f):
                writer.writerow([ row[x] for x in outList ])
            f.close()
            return response

        if 'downloadAll' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            f = open('dwn/merge.csv', 'r')
            outList = [ ele[3].split("_")[1] for ele in request.session['saved'] ]
            print(outList)
            outList = ['id1'] + outList 
            writer.writerow(outList)
            for row in csv.DictReader(f):
                writer.writerow([ row[x] for x in outList ])
            f.close()
            return response

    except:
        pass
    tags = {}
    data = {}
    out = []
    for rec in request.session['saved']:
        pk = rec[3].split('_')[0]
        tag = rec[3].split('_')[1]
        try:
            tags[pk].append(tag)
        except:
            tags[pk] = []
            tags[pk].append(tag)
        data[pk] = [rec[0], rec[1], rec[2], subject.objects.get(pk=pk).question ,"_".join(tags[pk])]
    for key in data:
        out.append(data[key])

    return render_to_response('download.html',{
        'saved': out,
    })
