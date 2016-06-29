from django.shortcuts import render_to_response

def dwn(request):
    try:
        if 'clear' in request.GET:
            request.session['saved'] = []
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
        data[pk] = [rec[0], rec[1], rec[2],str(tags[pk])]
    for key in data:
        out.append(data[key])

    return render_to_response('download.html',{
        'saved': out,
    })
