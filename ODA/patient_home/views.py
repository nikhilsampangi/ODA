from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Medical_shop, Stock_availability, General_Medicine, Blood_Bank, Blood_avail
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BloodavailSerializer,StockavailabilitySerializer
from rest_framework import status
from patient_home.decorators import only_patient
from . import forms
# Create your views here.


@only_patient
def home_page(request):
    return render(request, 'patient_home/home.html')

@only_patient
def doctor_list(request):
    return render(request, 'patient_home/doctors.html')

@only_patient
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

@only_patient
def my_appointments(request):
    return render(request, 'patient_home/my_appo.html')

@only_patient
def blood_bank(request):
    lat = Blood_Bank.objects.all().values_list('Lat')
    long = Blood_Bank.objects.all().values_list('Long')
    name = Blood_Bank.objects.all().values_list('BB_name')
    arry2 = []
    arry1 = []
    arry3 = []
    for i in lat:
        arry1 += [i[0]]
    for i in long:
        arry2 += [i[0]]
    for i in name:
        arry3 += [i[0]]
    print(arry1)
    print(arry2)
    print('aasfdsv')
    return render(request, 'patient_home/blood_banks.html', {'lat': arry1, 'lng': arry2, 'names': arry3})

@only_patient
def pharma_locator(request):
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
    return render(request, 'patient_home/pharma_loc.html', {'lat': arry1, 'lng': arry2, 'names': arry3})

@only_patient
def gen_meds(request):
    disease = General_Medicine.objects.all().values_list('Disease')
    medicine = General_Medicine.objects.all().values_list('Medicine')

    arry4 = []
    for i in disease:
        arry4 += [i[0]]
    arry5 = []
    for i in medicine:
        arry5 += [i[0]]
    print(arry4)
    print(arry5)
    return render(request, 'patient_home/gen_meds.html',
                  {'disease': arry4, 'medicine': arry5, 'ranges': zip(arry4, arry5)})




class Bloodbanklistview(APIView):
    def get(self,request):
        Bloodbank=Blood_avail.objects.all()
        serializer = BloodavailSerializer(Bloodbank,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = BloodavailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class Medicalshoplistview(APIView):
    def get(self,request):
        Bloodbank=Stock_availability.objects.all()
        serializer = StockavailabilitySerializer(Bloodbank,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = StockavailabilitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

@only_patient
def avail(request,shop_name):
    shopid=Medical_shop.objects.all().values_list('shop_id')
    names=Medical_shop.objects.all().values_list('shop_name')
    medicines=Stock_availability.objects.all().values_list('Medicine_name','shop_id')
    stock=Stock_availability.objects.all().values_list('Stock','shop_id')

    arry2=[]
    arry1=[]
    for i in names:
        arry1+=[i[0]]
    for i in shopid:
        arry2+=[i[0]]
    temp=0
    for i in arry1:
        if(i==shop_name):
            x=arry2[temp]
            break;
        temp+=1;
    arry1=[]
    arry2=[]
    arrylist=[]
    temp=0
    for i in medicines:
        print(i[1])
        if(x==i[1]):
            arry1+=[i[0]]
            arrylist+=[temp]
            temp=temp+1
    for i in stock:
        if(x==i[1]):
            arry2+=[i[0]]

    return render(request, 'patient_home/display_avail.html',{'name': shop_name,'id': x,'medicines': arry1,'stock': arry2,'range': zip(arry1,arry2)})

@only_patient
def getlocation(request):
    return render(request, 'patient_home/getlocation.html')

def mail(request):
    lat = '13.580023'
    long = '80.087543'
    send_mail(
        'EMERGENCY',
        'There is an emergency at location : ' + lat +' ' +long,
        'onlincedocapp@gmail.com',
        ['yashukikkuri@gmail.com'],
    );
    return render(request, 'patient_home/emergency.html')

def ProfileUpadate(request):
    if request.method == 'POST':
        # u_form = forms.UserUpdateForm(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, instance=request.user.patient_db)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
        return redirect('profile-upadate')
    else:
        # u_form = forms.UserUpdateForm(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.patient_db)


    return render(request, 'patient_home/patient_profile_update.html', {'p_form': p_form})