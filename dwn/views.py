from django.shortcuts import render_to_response
from sub.models import subject
from django.http import HttpResponse
import csv
# import os
# from xlrd import open_workbook

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
        if 'download' in request.GET:
            # filePath = './dwn/J1student/'
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'
            writer = csv.writer(response)
            for tag in request.GET['download'].split('_'):
                # for filename in os.listdir(filePath):
                    # book = open_workbook(filePath+filename)
                    # first_sheet = book.sheet_by_index(0)
                writer.writerow(["fuckyou!"])
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
