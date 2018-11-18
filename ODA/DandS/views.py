from django.shortcuts import render
from .models import Disease
from django.http import Http404

def index(request):
     diseases = Disease.objects.all()
     context = {'diseases':diseases}
     return render(request,'DandS/index.html',context)

def info(request,d_name):
    try:
        disease = Disease.objects.get(disease_name=d_name)
    except Disease.DoesNotExist:
        raise Http404("Disease not Found")
    return render(request,'DandS/info.html',{'disease':disease})
