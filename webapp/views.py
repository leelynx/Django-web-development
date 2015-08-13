#__*__ coding:utf-8 __*__
from django.shortcuts import render_to_response
import datetime
from django.shortcuts import render
from django.http import HttpResponse
import datetime

def curr_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def index(request):
    return render(request, 'index.html')

def add(request):
    a = request.GET['a']
    b = request.GET['b']
    a = int(a)
    b = int(b)
    sum = a + b
    return render(request, 'sum.html', {'sum': sum})
