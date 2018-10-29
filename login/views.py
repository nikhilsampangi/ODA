from django.shortcuts import render


# Create your views here.
def login_every(request):
    return render(request, 'login/login_every.html')
def login_doc(request):
    return  render(request, 'login/login_doc.html')
