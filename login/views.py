from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from login.models import Doctors
from login.models import Patient_DB
from django.contrib.auth.models import User


doc_type_list = {"doc_list": ['Audiologist ','Allergist','Andrologists ','Anesthesiologist ', 'Cardiologist ','Cardiovascular Surgeon' ,'Clinical Neurophysiologist ','Dentist ','Dermatologist ','Emergency Doctors','Endocrinologist ','Epidemiologists ','ENT Specialist ','Family Practitioner','Gastroenterologist ','Gynecologist ','General Psychiatrist','Hematologist ','Hepatologists ','Immunologist ','Infectious Disease Specialist','Internal Medicine Specialists','Internists ' ,'Medical Geneticist' ,'Microbiologist ' ,'Neonatologist ', 'Nephrologists ', 'Neurologist ', 'Neurosurgeons ','Obstetrician ' ,'Oncologist ', 'Ophthalmologist ' ,'Orthopedic Surgeon','Orthopedist ' ,'Primatologist ','Parasitologist ', 'Pathologists ','Pediatrician ' ,'Plastic Surgeon','Physiologists ','Physiatrist ','Podiatrists ','Psychiatrists ','Pulmonologist ','Radiologists ','Reproductive Endocrinologist','Urologist ','Veterinarian ']}

# Create your views here.
def login_every (request):
    return render(request, 'login/login_every.html')
def val_p(request):

    if request.method == 'POST':
        full_name = request.POST.get('Firstname')+' '+ request.POST.get('Lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone_num')
        age = request.POST.get('Age')
        gender = request.POST.get('Gender')
        blood_grp = request.POST.get('blood_grp')
        blood_type = request.POST.get('blood_type')
        emer_phone_num = request.POST.get('emer_phone_num')
        Medical = request.POST.get('Medical')
        blood = blood_grp + ' ' + blood_type
        user = User.objects.filter(email=email).first()


        #upadate the full name and delataeila



        p = Patient_DB(P_Id=user,Age=age, Gender=gender, Blood_group=blood, Phone_num=phone,
                   Emergency_num=emer_phone_num, medical_con=Medical,user='yes')
        p.save()

    return redirect('login:home-1')


def new_user(request):
    email = request.POST['email']

    full_name = request.POST['fullname']
    name_list = full_name.split(' ')
    firstname=name_list[0]
    lastname = name_list[1]
    image = request.POST['image']
    user = User.objects.filter(email=email).first()
    if User.objects.filter(email=email).exists():
        if Patient_DB.objects.filter(P_Id=user, user='yes').exists():
            return redirect('login:home-1')
        else:
            details = {'f_name': firstname, 'l_name': lastname, 'email': email}
            return render(request, 'login/cred_every.html', details)

    else:
        # p=Patient_DB(Name=full_name,Email_Id=email )
        user = User.objects.create_user(username=full_name,
                                        email= email,)
        user.save()
        request.method = 'GET'
        details={'f_name':firstname,'l_name':lastname ,'email':email}
        return render(request, 'login/cred_every.html',details)

def home(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('f_name')).exists():
            print('sdfasdfa')
            return  render(request, 'login/home.html', {'f_name': request.POST.get('f_name')})

    return render(request,'login/home.html')

def cred_doc(request):
    if request.method == 'POST':
        firstname = request.POST.get('Firstname')
        lastname = request.POST.get('Lastname')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        phone = request.POST.get('phone_num')
        gender = request.POST.get('gender')
        l_num=request.POST.get('licence')
        doc_type=request.POST.get('Doctor Type')
        doc_deg=request.POST.get('Doctor_Deg')
        if User.objects.filter(email=email).exists():
            return redirect('login:home-1')
        else :
            user=User.objects.create_user(username=firstname+''+lastname,
                                          email=email,
                                          password=password,)
            d=Doctors(D_Id=user,Phone=phone,gender=gender,Degrees=doc_deg,Latitudes=123,Longitudes=12,Avail=1)
            d.save()
        return render(request,'login/cred_doc.html',doc_type_list)
    return render(request,'login/cred_doc.html',doc_type_list)


def login_doc(request):
    if request.method == 'POST':
        email = request.POST.get('doc_email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        usr = user.username
        print(usr)
        user = authenticate(username=usr, password=password)

        if user:
            # if user.is_active:
            login(request, user)
            return redirect('login:home-1')
        else:
            return HttpResponse('fail')
    return render(request, 'login/login_doc.html')

