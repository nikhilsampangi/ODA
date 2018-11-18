from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from welcome.models import Doctors,Patient_DB

doc_type_list = {"doc_list": ['Audiologist ', 'Allergist', 'Andrologists ', 'Anesthesiologist ', 'Cardiologist ',
                              'Cardiovascular Surgeon', 'Clinical Neurophysiologist ', 'Dentist ', 'Dermatologist ',
                              'Emergency Doctors', 'Endocrinologist ', 'Epidemiologists ', 'ENT Specialist ',
                              'Family Practitioner', 'Gastroenterologist ', 'Gynecologist ', 'General Psychiatrist',
                              'Hematologist ', 'Hepatologists ', 'Immunologist ', 'Infectious Disease Specialist',
                              'Internal Medicine Specialists', 'Internists ', 'Medical Geneticist', 'Microbiologist ',
                              'Neonatologist ', 'Nephrologists ', 'Neurologist ', 'Neurosurgeons ', 'Obstetrician ',
                              'Oncologist ', 'Ophthalmologist ', 'Orthopedic Surgeon', 'Orthopedist ', 'Primatologist ',
                              'Parasitologist ', 'Pathologists ', 'Pediatrician ', 'Plastic Surgeon', 'Physiologists ',
                              'Physiatrist ', 'Podiatrists ', 'Psychiatrists ', 'Pulmonologist ', 'Radiologists ',
                              'Reproductive Endocrinologist', 'Urologist ', 'Veterinarian ']}


def home(request):
    # if request.method == 'POST':
    #     if User.objects.filter(username=request.POST.get('f_name')).exists():
    #         print('sdfasdfa')
    #         return render(request, 'welcome/home.html', {'f_name': request.POST.get('f_name')})
    return render(request, 'welcome/home.html')


def front_page(request):
    return render(request, 'welcome/main_page.html')


def doctor_page(request):
    if request.user.is_authenticated:
       return redirect('welcome:home')
    return render(request, 'welcome/doc_log.html')


def doc_login(request):
    if request.method == 'POST':
        email = request.POST.get('doc_email')
        password = request.POST.get('doc_pass')
        user = User.objects.filter(email=email).first()
        usr = user.username
        user = authenticate(username=usr, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('welcome:home')
            else:
                return redirect('welcome:home')
        else:
            return HttpResponse('fail')


def doc_register(request):
    if request.user.is_authenticated:
        redirect('welcome:home')
    if request.method == 'POST':
        firstname = request.POST.get('f_name')
        lastname = request.POST.get('l_name')
        username=firstname + '' + lastname
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone_num')
        gender = request.POST.get('gender')
        l_num = request.POST.get('license')
        doc_type = request.POST.get('Doctor Type')
        doc_deg = request.POST.get('Doctor_Deg')
        print(password)
        print(l_num)
        print(phone)
        print(gender)

        if User.objects.filter(email=email).exists():
            return redirect('welcome:home')
        else:
            user = User.objects.create_user(username=username,
                                            email=email,
                                            password=password, )
            d = Doctors(D_Id=user, Phone=phone, license=l_num ,gender=gender, Degrees=doc_deg, Latitudes=123, Longitudes=12, Avail=1)
            d.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                else:
                    pass
            return redirect('welcome:home')
    return render(request, 'welcome/doc_log.html', doc_type_list)

def val_user(request):
    if request.method == 'POST':
        full_name = request.POST.get('Firstname')+' '+ request.POST.get('Lastname')
        emergency_email = request.POST.get('emer_email')
        email = request.POST.get('email')
        phone = request.POST.get('phone_num')
        age = request.POST.get('Age')
        gender = request.POST.get('gender')
        blood_grp = request.POST.get('blood')
        blood_type = request.POST.get('blood_type')
        emer_phone_num = request.POST.get('emer_phone_num')
        Medical = request.POST.get('med_cond')
        blood = blood_grp + ' ' + blood_type
        image_url=request.POST.get('image_url')
        user = User.objects.filter(email=email).first()
        password = 'qwert12345'


        #upadate the full name and delataeila



        p = Patient_DB(P_Id=user, Age=age, Gender=gender, Blood_group=blood, Phone_num=phone,
                   Emergency_num=emer_phone_num, medical_con=Medical,image_url=image_url,user_ava='yes')
        p.save()

        user_auth = authenticate(username=user.username, password=password)

        if user_auth:
            if user_auth.is_active:
                login(request, user_auth)
                return redirect('welcome:home')
        else:
            return HttpResponse('fail')
    return render(request,'welcome/pat_reg.html')
def patient_reg(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['fullname']
        name_list = full_name.split(' ')
        firstname = name_list[0]
        lastname = name_list[1]
        image = request.POST['image']

        print('goku : '+image)

        password = 'qwert12345'
        if User.objects.filter(email=email).exists():
            user = User.objects.filter(email=email).first()
            if Patient_DB.objects.filter(P_Id=user, user_ava='yes').exists():
                if request.user.is_authenticated:
                    return redirect('welcome:home')
                else:
                    user_auth = authenticate(username=user.username, password=password)

                    if user_auth:
                        if user_auth.is_active:
                            login(request, user_auth)
                            return redirect('welcome:home')
                    else:
                        return HttpResponse('fail')

            else:
                details = {'f_name': firstname, 'l_name': lastname, 'email': email,'image': image}
                return render(request, 'welcome/pat_reg.html', details)
        else:
            user = User.objects.create(username=full_name,
                                            email=email, )
            user.set_password(password)
            user.save()
            user = User.objects.filter(email=email).first()

            request.method = 'GET'
            details = {'f_name': firstname, 'l_name': lastname, 'email': email ,'image': image}
            return render(request, 'welcome/pat_reg.html', details)
    else:
        return render(request, 'welcome/pat_log.html')

def patient_log(request):
    if request.user.is_authenticated:
        return redirect('welcome:home')
    else:
        return render(request, 'welcome/pat_log.html')