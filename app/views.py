from django.shortcuts import render

# Create your views here.
from app.models import *

from app.forms import *

from django.http import HttpResponse


def insert_topic(request):
    EFTO=TopicForm()
    d={'EFTO':EFTO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            EFTO=Topics.objects.all()
            d1={'EFTO':EFTO}
            return render(request,'display_topic.html',d1)

    return render(request,'insert_topic.html',d)
def display_topic(request):
    EFTO=Topics.objects.all()
    d1={'EFTO':EFTO}
    return render(request,'display_topic.html',d1)

def insert_webpage(request):
    WFTO=WebpageForm()
    d={'WFTO':WFTO}
    if request.method=='POST':
        VFTO=WebpageForm(request.POST)
        if VFTO.is_valid():
            VFTO.save()
            WFTO=Webpage.objects.all()
            d1={'WFTO':WFTO}
            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)