from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
    return render(request, 'patient_home/home.html')

def doctor_list(request):
    return render(request, 'patient_home/doctors.html')

def doctor_locator(request):
    return render(request, 'patient_home/doc_loc.html')

def my_appointments(request):
    return render(request, 'patient_home/my_appo.html')

def blood_bank(request):
    return render(request, 'patient_home/pharma_loc.html')

