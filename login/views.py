from django.shortcuts import render

from login.models import Patient_DB

# Create your views here.
def login_every(request):
    return render(request, 'login/login_every.html')
def login_doc(request):
    return  render(request, 'login/login_doc.html')
def cred_every(request):
    if request.method == 'POST':
        firstname = request.POST.get('Firstname')
        lastname = request.POST.get('Lastname')
        phone = request.POST.get('phone_num')
        age = request.POST.get('Age')
        Gender = request.POST.get('Gender')
        blood_grp = request.POST.get('blood_grp')
        blood_type = request.POST.get('blood_type')
        emer_phone_num = request.POST.get('emer_phone_num')
        Medical = request.POST.get('Medical')

        email = request.POST.get('Lastname')
        print(firstname)

        submitbutton = request.POST.get('Submit')
        Full_name = firstname+' '+lastname
        blood=blood_grp+ ' ' + blood_type
        p = Patient_DB(Name=Full_name, Age=age, Gender=Gender, Blood_group=blood, Phone_num=phone, Emergency_num=emer_phone_num, Email_Id= email, medical_con= Medical)
        p.save()

    return render(request, 'login/cred_every.html')
def cred_doc(request):

    return  render(request,'login/cred_doc.html')
