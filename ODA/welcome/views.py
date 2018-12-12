from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from welcome.models import Doctors
from welcome.models import Doctors,Patient_DB,Appointment
from patient_home import views
from welcome.decorators import *
from . import forms
from django.core.mail import send_mail



from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context




import os
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from email.mime.image import MIMEImage




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
                              'Reproductive Endocrinologist', 'Urologist ', 'Veterinarian '],
                 "doc_deg": ['MBBS', 'BDS','BHMS', 'BAMS', 'DHMS', 'BUMS', 'BVSc & AH', 'B. Pharm', 'BOT', 'BMLT','BPT',
                            'B.Sc. Nursing', 'BNYS']}



# Create your views here.
# def logout_user(request):
#     if request.user.is_authenticated:
#         logout(request)
#         return redirect('welcome:home')
#     else:
#         return redirect('welcome:home')
@only_doctor
def home(request):
    # pi=request.user.doctors.pk
    # print(pi)
    # lati=Appointment.objects.all().values_list('P_Id','Date','D_Id')
    # arry1=[]
    # arry2=[]
    # print(lati)
    # for i in lati:
    #     if(i[2]==pi):
    #         arry1+=[i[1]]
    #         arry2+=[i[0]]
    # print(arry2)
    # pi=request.user.doctors.T_Id
    # print(pi)
    pi=request.user.doctors.D_Id
    lati=Appointment.objects.all().values_list('P_Id','Date','D_Id','slots')
    arry1=[]
    arry2=[]
    arry2_1=[]
    arry2_2=[]
    arry2_3=[]
    arry3=[]
    k=Doctors.objects.get(pk=pi)
    for i in lati:
        k=Doctors.objects.get(pk=i[2])
        print(i)
        print(type(i[0]))
        if(k.D_Id==pi):
            p=i[1].split('-')
            print(p)
            print(p[0])
            arry2_1+=[p[0]]
            arry2_2+=[p[1]]
            arry2_3+=[p[2]]
            arry3+=[i[3]]
            doc=Patient_DB.objects.get(pk=i[0])
            arry2+=[doc.P_Id.username]
    print(arry2_1)
    print(arry3)
    print(arry1)
    print(arry2)
    return render(request, 'welcome/home.html',{'pat':arry2 , 'year':arry2_1 , 'mon':arry2_2 ,'da':arry2_3,'slo':arry3 })
    # return render(request, 'welcome/home.html',{'lat':zip(arry1,arry2)})

@user_not_auth
def front_page(request):
    return render(request, 'welcome/main_page.html')

@user_not_auth
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
        if(User.objects.filter(email=email).exists()):
            password = request.POST.get('doc_pass')
            user = User.objects.filter(email=email).first()

            user = authenticate(username=user.username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('welcome:home')
                else:
                    return redirect('welcome:home')
            else:
                messages.error(request, f'INVALID EMAIL OR PASSWORD')
                return redirect('welcome:doc-l-r')
        else:
            messages.error(request, f'INVALID EMAIL')
            return redirect('welcome:doc-l-r')

    else:
        raise PermissionDenied


def doc_register(request):
    if request.user.is_authenticated:
        return redirect('welcome:frontpage')
    if request.method == 'POST':
        print("111111")
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
        lat = request.POST.get('lat')
        log = request.POST.get('log')

        lat=float(lat);
        long=float(log);
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
            d = Doctors(D_Id=user,Phone=phone, license=l_num, gender=gender, Degrees=doc_deg, Latitudes=lat,
                        Longitudes=long, Avail=1,Spec=doc_type)
            d.save()

            htmly = get_template('patient_home/mail2.html')
            html_content=htmly.render()

            msg = EmailMultiAlternatives('Welcome', 'Have a look at what all you can do in ODA', 'onlinedocapp@gmail.com', [email])


            msg.mixed_subtype = 'related'

            for f in ['patient_home/images/ODA-06-06.png']:
                fp = open(os.path.join(os.path.dirname("/Users/KIKKURI/Desktop/asenewpro/ODA-2/ODA/patient_home/static/"), f), 'rb')
                msg_img = MIMEImage(fp.read())
                fp.close()
                msg_img.add_header('Content-ID', '<{}>'.format(f))
                msg.attach(msg_img)

            msg.attach_alternative(html_content, "text/html")
            msg.send()




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
        if User.objects.filter(email=request.user.email).exists():
            name = User.objects.filter(email=request.user.email).first()
            if Doctors.objects.filter(D_Id=name).exists():
                messages.error(request, f'Email already exists try using other email')     ##add in html
                return redirect('welcome:logout')
            else:
                pass
        if request.method == 'POST':
            emergency_email = request.POST.get('emer_email')
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
            # password = 'qwert12345'
            # print('username :')
            # print(user.username)
            # upadate the full name and delataeila

            p = Patient_DB(P_Id=user, Age=age, Gender=gender, Blood_group=blood, Phone_num=phone,emerg_email=emergency_email,
                           Emergency_num=emer_phone_num, medical_con=Medical, user_pat='yes')
            p.save()

            htmly = get_template('patient_home/mail1.html')
            html_content=htmly.render()

            msg = EmailMultiAlternatives('Welcome', 'Have a look at what all you can do in ODA', 'onlinedocapp@gmail.com', [str(request.user.email)])


            msg.mixed_subtype = 'related'

            for f in ['patient_home/images/ODA-05.png']:
                fp = open(os.path.join(os.path.dirname("/Users/KIKKURI/Desktop/asenewpro/ODA-2/ODA/patient_home/static/"), f), 'rb')
                msg_img = MIMEImage(fp.read())
                fp.close()
                msg_img.add_header('Content-ID', '<{}>'.format(f))
                msg.attach(msg_img)

            msg.attach_alternative(html_content, "text/html")
            msg.send()




            return render(request, 'patient_home/home.html')
        else:
            return render(request, 'welcome/pat_log.html')

    return render(request, 'welcome/pat_log.html')


@only_doctor
def pro_upd_doc(request):
    if request.method == 'POST':
        user_form = forms.User_update_Form(request.POST, instance=request.user)
        d_form = forms.DoctorUpdateForm(request.POST, instance=request.user.doctors)
        if d_form.is_valid() and user_form.is_valid():
            user_form.save()
            d_form.save()
            messages.success(request, f'Your account has been updated successfully!')
            return redirect('welcome:home')
    else:
        user_form = forms.User_update_Form(instance=request.user)
        d_form = forms.DoctorUpdateForm(instance=request.user.doctors)

    return render(request, 'welcome/profile_update_doctor.html', {'d_form': d_form,'u_form':user_form})


@only_doctor
def loc_win(request):
    return render('welcome/loc_win.html')

@only_doctor
def schedule(request):
    pi=request.user.doctors.D_Id
    lati=Appointment.objects.all().values_list('P_Id','Date','D_Id','slots')
    arry1=[]
    arry2=[]
    arry2_1=[]
    arry2_2=[]
    arry2_3=[]
    arry3=[]
    k=Doctors.objects.get(pk=pi)
    for i in lati:
        k=Doctors.objects.get(pk=i[2])
        print(i)
        print(type(i[0]))
        if(k.D_Id==pi):
            p=i[1].split('-')
            print(p)
            print(p[0])
            arry2_1+=[p[0]]
            arry2_2+=[p[1]]
            arry2_3+=[p[2]]
            arry3+=[i[3]]
            doc=Patient_DB.objects.get(pk=i[0])
            arry2+=[doc.P_Id.username]
    print(arry2_1)
    print(arry3)
    print(arry1)
    print(arry2)

    return render(request, 'welcome/schedule.html',{'pat':arry2 , 'year':arry2_1 , 'mon':arry2_2 ,'da':arry2_3,'slo':arry3 })
