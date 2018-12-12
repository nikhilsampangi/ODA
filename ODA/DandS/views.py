from django.shortcuts import render
from .models import Disease
from django.http import Http404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q


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

def search(request):
    if request.method=="POST":
        query = request.POST['search_box']

        if query:
            match = Disease.objects.filter(Q(symptoms__symptom__iexact=query) | Q(disease_name__icontains=query) | Q(disease_part__iexact=query))
            match_unique=list(set(match))

            if match:
                return render(request,'DandS/search.html',{'match_unique':match_unique})
            else:
                messages.error(request,'No results found')
        else:
            return HttpResponseRedirect('.')

    return render(request,'DandS/search.html')
