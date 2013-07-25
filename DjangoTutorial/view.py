from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime
import csv
from reportlab.pdfgen import canvas
from cStringIO import StringIO

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

# Number of unruly passengers each year 1995 - 2005. In a real application
# this would likely come from a database or some other back-end data store.
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]
def unruly_passengers_csv(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'
    
    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2005), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response

def hello_pdf(request):
    response = HttpResponse(mimetype='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    
    tempPdf = StringIO()
    
    pdf = canvas.Canvas(tempPdf)
    pdf.drawString(100, 700, 'Hello world!')
    
    pdf.showPage()
    pdf.save()
    
    response.write(tempPdf.getvalue())
    
    return response

def hello_video(request):    
    return render_to_response('video.html')