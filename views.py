from django.http import HttpResponse
from django.shortcuts import render
from diseaseidentification.models import latlng

def nearby(request):
    lati=latlng.objects.all().values_list('lat')
    longi=latlng.objects.all().values_list('lng')
    arry2=[]
    arry1=[]
    for i,j in lati,longi:
        arry1+=[i[0]]
        arry2+=[j[0]]
    print(arry1)
    print(arry2)
    return render(request, 'Map.html',{'lat': arry1,'lng': arry2})

# Add the two views we have been talking about  all this time :)
def current(request):
    return render(request, 'Mapplot.html')

def first_page(request):
    lati=latlng.objects.all().values_list('lat')
    longi=latlng.objects.all().values_list('lng')
    arry2=[]
    arry1=[]
    for i,j in lati,longi:
        arry1+=[i[0]]
        arry2+=[j[0]]
    print(arry1)
    print(arry2)
    return render(request, 'check.html',{'lat': arry1,'lng': arry2})
