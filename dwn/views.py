from django.shortcuts import render_to_response
from sub.models import subject
from django.http import HttpResponse
import csv
from glob import glob

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
        if 'download' in request.GET:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            for tag in request.GET['download'].split('_'):
                for filename in glob('./dwn/J1student/*.csv'):
                    f = open(filename, 'r')
                    for row in csv.reader(f):
                        if row[0] == tag:
                            writer.writerow(row)
                            break
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
