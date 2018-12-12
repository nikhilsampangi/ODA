from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Medical_shop, Stock_availability, General_Medicine, Blood_Bank, Blood_avail,tips,facts
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
from welcome.models import Patient_DB,Doctors,Appointment




from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context




import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage





@only_patient
def home_page(request):
    pi=request.user.patient_db.pk
    print(pi)
    lati=Appointment.objects.all().values_list('P_Id','Date','D_Id')
    arry1=[]
    arry2=[]
    for i in lati:
        if(i[0]==pi):
            arry1+=[i[1]]
            doc=Doctors.objects.get(pk=i[2])
            print(doc)
            arry2+=[doc]
    tip = tips.objects.all().values_list('tip')
    arry3 = []
    for i in tip:
        arry3 += [i[0]]
    fact = facts.objects.all().values_list('fact')
    arry4 = []
    for i in tip:
        arry4 += [i[0]]

    return render(request, 'patient_home/home.html',{'dte': zip(arry1,arry2),'tip':arry3,'fact':arry4,'doc':[arry2[0]]})

@only_patient
def doctor_list(request):
    lati=Doctors.objects.all()
    arry1=[]
    arry2=[]
    for i in lati:
        arry1+=[i.D_Id]
        arry2+=[i.Spec]
    return render(request, 'patient_home/doctors.html',{'lat':zip(arry1,arry2)})

@only_patient
def doctor_locator(request):
    lati = Doctors.objects.all().values_list('Latitudes')
    longi = Doctors.objects.all().values_list('Longitudes')
    names=Doctors.objects.all()
    arry2 = []
    arry1 = []
    arry3 = []
    print('111')
    for i in lati:
        arry1 += [i[0]]
    for i in longi:
        arry2 += [i[0]]
    for i in names:
        k=str(i.D_Id)
        arry3+=[k]
    print(arry1)
    print(arry2)
    print(arry3)
    return render(request, 'patient_home/doc_loc.html', {'lat': arry1, 'lng': arry2, 'names': arry3})

@only_patient
def my_appointments(request):
    pi=request.user.patient_db.pk
    print(pi)
    lati=Appointment.objects.all().values_list('P_Id','Date','D_Id')
    arry1=[]
    arry2=[]
    for i in lati:
        if(i[0]==pi):
            arry1+=[i[1]]
            doc=Doctors.objects.get(pk=i[2])
            print(doc)
            arry2+=[doc]
    return render(request, 'patient_home/my_appo.html',{'dte': zip(arry1,arry2)})

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
    print(arry1)
    print(arry2)
    print(arry3)
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

def mail(request,lat,long):


    pi=request.user.patient_db.emerg_email
    print(type(pi))
    print(str(pi))
    print(type(pi))
    print(pi)


    u=request.user.username
    send_mail(
        'EMERGENCY',
        'There is an emergency for '+ u +' at location : ' + lat +' ' +long,
        'onlincedocapp@gmail.com',
        [str(pi)],
    );
    return render(request, 'patient_home/emergency.html')
@only_patient
def ProfileUpadate(request):
    if request.method == 'POST':
        u_form = forms.User_update_Form(request.POST, instance=request.user)
        p_form = forms.ProfileUpdateForm(request.POST, instance=request.user.patient_db)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated successfully!')
        return redirect('pat_home_page')
    else:
        u_form = forms.User_update_Form(instance=request.user)
        p_form = forms.ProfileUpdateForm(instance=request.user.patient_db)

    return render(request, 'patient_home/patient_profile_update.html', {'p_form': p_form,'u_form':u_form})


def take_appo(request):
    doc=request.POST.get('doct')
    docto=doc.split('.')
    doct=docto[1].split('-')
    print(doct[0])
    arry1=[doct[0]]
    arry4=[doct[1]]
    request.session['doc']=doct[0]
    date=Appointment.objects.all().values_list('Date','slots','D_Id')
    arry2_1=[]
    arry2_2=[]
    arry2_3=[]
    arry3=[]
    p=arry1[0]
    p=p[0:len(p)-1]
    for i in date:
        k=Doctors.objects.get(pk=i[2])
        if(str(k)==p):
            k=i[0].split('-')
            print(k)
            print(k[0])
            arry2_1+=[k[0]]
            arry2_2+=[k[1]]
            arry2_3+=[k[2]]
            arry3+=[i[1]]
    print(arry2_1)
    print(arry3)
    k=Doctors.objects.get(pk=i[2])
    p=str(k.Phone)
    a=str(k.About_Clinic)
    i=str(k.Other_info)
    e=str(k.d_website)
    d=str(k.Desc)
    return render(request, 'patient_home/doctor_profile.html',{'doc':arry1,'year':arry2_1,'mon':arry2_2,'da':arry2_3,'slo':arry3,'spec':arry4,'about':[a],'phone':[p],'info':[i],'email':[e],'desc':[d]})

def appo(request,doctor):
    arry1=[doctor]
    request.session['doct']=doctor
    return render(request, 'patient_home/doctor_profile.html',{'doc':arry1})


def book(request):
    tie=request.POST['time']
    dae=request.POST['date']
    patient=request.user.patient_db
    arry1=[]
    lati=Doctors.objects.all()
    doc=request.session['doc']
    doc=doc[0:len(doc)-1]
    for i in lati:

        print(doc)
        print(len(doc))
        print(len(str(i.D_Id)))
        print(type(str(i.D_Id)))
        if(doc==str(i.D_Id)):
            arry1=[i.D_Id]

    arry2=[]
    lati=Patient_DB.objects.all()
    for i in lati:
        if(i.P_Id==patient.P_Id):
            arry2+=[i.P_Id]
    doct=Doctors.objects.get(pk=arry1[0])
    d=Appointment(P_Id=patient,D_Id=doct,Date=dae,slots=tie)
    d.save()
    return render(request,"patient_home/booking_success.html" , {'dat':[dae],'doc':[doct]})


def booked(request,doc):
    tie=request.POST['time']
    dae=request.POST['date']
    patient=request.user.patient_db
    arry1=[]
    lati=Doctors.objects.all()
    doc=request.session['doct']
    for i in lati:
        if(doc==str(i.D_Id)):
            arry1=[i.D_Id]

    arry2=[]
    lati=Patient_DB.objects.all()
    for i in lati:
        if(i.P_Id==patient.P_Id):
            arry2+=[i.P_Id]
    doct=Doctors.objects.get(pk=arry1[0])
    d=Appointment(P_Id=patient,D_Id=doct,Date=dae,slots=tie)
    d.save()
    return render(request,"patient_home/booking_success.html")

def pharma_stock(request):
    return render(request, "patient_home/stock_availability.html")

def about(request):
    return render(request, "patient_home/about_page.html")

def doc_ident(request):
    lati=Doctors.objects.all()
    arry1=[]
    arry2=[]
    for i in lati:
        arry1+=[i.D_Id]
        arry2+=[i.Spec]
    return render(request, "patient_home/doctor_identification.html",{'ranges':zip(arry1,arry2)})

def doc(request):
    name=request.POST['doct']
    lati=Doctors.objects.all()
    arry1=[]
    arry2=[]
    for i in lati:
        if(str(i.Spec)==str(name)):
            arry1+=[i.D_Id]
    print(arry1)
    return HttpResponse(request, "patient_home/doctor_identification.html",{'ranges':arry1})

def bloodavail(request,bank_name):
    shopid=Blood_Bank.objects.all().values_list('BB_id')
    names=Blood_Bank.objects.all().values_list('BB_name')
    medicines=Blood_avail.objects.all().values_list('Blood_grp','BB_id')
    stock=Blood_avail.objects.all().values_list('Availability','BB_id')

    arry2=[]
    arry1=[]
    for i in names:
        arry1+=[i[0]]
    for i in shopid:
        arry2+=[i[0]]
    temp=0
    for i in arry1:
        if(i==bank_name):
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

    return render(request, 'patient_home/display_avail.html',{'name': bank_name,'id': x,'medicines': arry1,'stock': arry2,'range': zip(arry1,arry2)})

def faq(request):
    return render(request, 'patient_home/faq.html')