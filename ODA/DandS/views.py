from django.shortcuts import render
from .models import Disease
from django.http import Http404

def linking(request):
    return render(request,'DandS/Linking.html')

def info(request,body_part,d_name):
    try:
        disease = Disease.objects.get(disease_name=d_name)
    except Disease.DoesNotExist:
        raise Http404("Disease not Found")
    return render(request,'DandS/info.html',{'disease':disease})

def index(request,body_part):
    diseases = Disease.objects.filter(disease_part=body_part)
    context = {'diseases': diseases, 'body_part': body_part}
    return render(request, 'DandS/index.html', context)