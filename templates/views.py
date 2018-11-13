from django.http import HttpResponse
from django.shortcuts import render
from diseaseidentification.models import latlng,tips,General_Medicine,Stock_availability,Medical_shop,Blood_Bank,Blood_avail
from django.core.mail import send_mail

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
    return render(request, 'check.html',{'lat': arry1,'lng': arry2})

def extratips(request):
    tip=tips.objects.all().values_list('tip')
    arry1=[]
    for i in tip:
        arry1+=[i[0]]
    return render(request,'tips.html',{'tips':arry1})

def getlocation(request):
#    getlocation=request.POST['getlocation']
    return render(request,'getlocation.html')

def sendingmail(request):

    send_mail(
        'Notifying your appointment',
        'You have an appointment in half an hour http://127.0.0.1:8000/diseaseidentification/tips',
        'onlinedocapp@gmail.com',
        ['yashukikkuri@gmail.com'],
        fail_silently=False,
    )
    return render(request,'sendingmail.html')

def medicalshop(request):
    lati=Medical_shop.objects.all().values_list('Lattitude')
    longi=Medical_shop.objects.all().values_list('Longitude')
    names=Medical_shop.objects.all().values_list('shop_name')
    arry2=[]
    arry1=[]
    arry3=[]
    for i in lati:
        arry1+=[i[0]]
    for i in longi:
        arry2+=[i[0]]
    for i in names:
        arry3+=[i[0]]
    return render(request, 'medicalshop.html',{'lat': arry1,'lng': arry2,'names': arry3})

def shopname(request,shop_name):
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

    return render(request, 'display_shop.html',{'name': shop_name,'id': x,'medicines': arry1,'stock': arry2,'range': zip(arry1,arry2)})




def bloodbank(request):
    lati=Blood_Bank.objects.all().values_list('Lat')
    longi=Blood_Bank.objects.all().values_list('Long')
    names=Blood_Bank.objects.all().values_list('BB_name')
    arry2=[]
    arry1=[]
    arry3=[]
    for i in lati:
        arry1+=[i[0]]
    for i in longi:
        arry2+=[i[0]]
    for i in names:
        arry3+=[i[0]]
    return render(request, 'bloodbanks.html',{'lat': arry1,'lng': arry2,'names': arry3})

def bankname(request,bank_name):
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

    return render(request, 'display_shop.html',{'name': bank_name,'id': x,'medicines': arry1,'stock': arry2,'range': zip(arry1,arry2)})

def eye(request):

    return render(request, 'eye.html')

def ear(request):

    return render(request, 'ear.html')
