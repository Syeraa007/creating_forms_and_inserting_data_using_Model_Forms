from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
# Create your views here.
def topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        return HttpResponse('Data taken')
    return render(request,'topic.html',d)

def page(request):
    PFO=PageForm()
    d={'PFO':PFO}
    if request.method=='POST':
        PFD=PageForm(request.POST)
        if PFD.is_valid():
            PFD.save()
        return HttpResponse('Data taken')
    return render(request,'page.html',d)

def record(request):
    RFO=RecordForm()
    d={'RFO':RFO}
    if request.method=='POST':
        RFD=RecordForm(request.POST)
        if RFD.is_valid():
            RFD.save()
        return HttpResponse('Data taken')
    return render(request,'record.html',d)