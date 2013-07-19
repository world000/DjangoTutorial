from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

def my_homepage_view(request):
    return HttpResponse("Hello, This is home page!")

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
    current_date = datetime.datetime.now()
    context = locals()
    del context['request']
    
    return render_to_response('current_datetime.html', context)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    
    return render_to_response('hours_ahead.html', {'next_time' : dt, 'hour_offset' : offset})

def display_meta(request):
    meta = request.META.items()
    meta.sort()
    return render_to_response('display_meta.html', {'meta' : meta})

def mobile(request):
    return render_to_response('mobile.html', {'data' : 'hello world'})

# named group practice.
def year_archive(request, year, month):
    return HttpResponse('NOT group year = %s, month = %s' % (year, month))

def month_archive(request, year, month):
    return HttpResponse('group year = %s, month = %s' % (year, month))
