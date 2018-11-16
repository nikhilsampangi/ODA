from django.shortcuts import render
from .models import Medical_shop, Stock_availability, General_Medicine, Blood_Bank, Blood_avail

from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'patient_home/home.html')

def doctor_list(request):
    return render(request, 'patient_home/doctors.html')

def doctor_locator(request):
    lati = Medical_shop.objects.all().values_list('Lattitude')
    longi = Medical_shop.objects.all().values_list('Longitude')
    names = Medical_shop.objects.all().values_list('shop_name')
    arry2 = []
    arry1 = []
    arry3 = []
    for i in lati:
        arry1 += [i[0]]
    for i in longi:
        arry2 += [i[0]]
    for i in names:
        arry3 += [i[0]]
    return render(request, 'patient_home/doc_loc.html', {'lat': arry1, 'lng': arry2, 'names': arry3})


def my_appointments(request):
    return render(request, 'patient_home/my_appo.html')

def blood_bank(request):
    return render(request, 'patient_home/pharma_loc.html')

