from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from welcome.models import Doctors
from welcome.models import Doctors,Patient_DB
from patient_home import views
from welcome.decorators import only_doctor


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



# Create your views here.
# def logout_user(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect('welcome:home')
#     else:
#         return redirect('welcome:home')
@only_doctor
def home(request):
    if request.user.is_authenticated:
        try:
            if request.user.doctors.user_pat == 'no':
                return render(request, 'welcome/home.html')
        except:
                return redirect('welcome:pat_log')
    return render(request, 'welcome/home.html')


def front_page(request):
    if request.user.is_authenticated:
        raise PermissionError
    return render(request, 'welcome/main_page.html')


def doctor_page(request):
    if request.user.is_authenticated:
        try:
            if request.user.doctors.user_pat == 'no':
                return redirect('welcome:home')
        except:
                return redirect('welcome:pat_log')
    return render(request, 'welcome/doc_log.html',doc_type_list)


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
        return redirect('welcome:frontpage')
    if request.method == 'POST':
        firstname = request.POST.get('f_name')
        lastname = request.POST.get('l_name')
        username = firstname + '' + lastname
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
            d = Doctors(D_Id=user, Phone=phone, license=l_num, gender=gender, Degrees=doc_deg, Latitudes=123,
                        Longitudes=12, Avail=1)
            d.save()
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                else:
                    pass
            return redirect('welcome:home')
    return render(request, 'welcome/doc_log.html', doc_type_list)


def pat_log(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            emergency_email = request.POST.get('em_mail')
            phone = request.POST.get('phone_num')
            em_phone_num=request.POST.get('em_phone_num')
            age = request.POST.get('Age')
            gender = request.POST.get('gender')
            blood_grp = request.POST.get('blood')
            blood_type = request.POST.get('blood_type')
            emer_phone_num = request.POST.get('emer_phone_num')
            Medical = request.POST.get('med_cond')
            blood = blood_grp + ' ' + blood_type
            user = User.objects.filter(email=request.user.email).first()
            password = 'qwert12345'
            print('username :')
            print(user.username)
            # upadate the full name and delataeila

            p = Patient_DB(P_Id=user, Age=age, Gender=gender, Blood_group=blood, Phone_num=phone,
                           Emergency_num=emer_phone_num, medical_con=Medical, user_pat='yes')
            p.save()
            return render(request, 'patient_home/home.html')
        else:
            return render(request, 'welcome/pat_log.html')

    return render(request, 'welcome/pat_log.html')
