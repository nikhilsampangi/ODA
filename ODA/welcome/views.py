from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def front_page(request):
    return render(request, 'welcome/main_page.html')

def doctor_page(request):
    return render(request, 'welcome/doc_log.html')
