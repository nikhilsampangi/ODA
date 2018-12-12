import openpyxl as openpyxl
import required as required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic
from Registration.tokens import  password_reset_token
from .models import Medical,Stock
# Create your views here.
from patient_home.models import Stock_availability,Medical_shop
from Registration.forms import UserInfoForm,PasswordResetForm,SetNewPasswordForm

"""
class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    #template_name = 'signup.html'
"""
def homepage(request):
    return render(request , "Registration/home.html")

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserInfoForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else :
            print(user_form.errors)
    else:
        user_form = UserInfoForm()
    return render(request,'Registration/signup.html',{'user_form':user_form,'registered':registered})


def userlogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)
        print(user)
        if user:
            print("not none")
            if user.is_active:
                print("logging in")
                login(request,user)
                return render(request,'Registration/home.html')
            else:
                return HttpResponse("Not Active.....Reload and try again...")
        else:
            return HttpResponse("...Invalid details...")
    else:
        return render(request, 'Registration/login.html', {})


@login_required
def userlogout(request):
    logout(request)
    return render(request,'Registration/home.html')


def change_user_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('Email')
            user = User.objects.get(email=email)
            if user:
                current_site = get_current_site(request)
                mail_subject = 'Reset Your Password'
                message = render_to_string('Registration/email_password_reset.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': password_reset_token.make_token(user),
                })
                to_email = form.cleaned_data.get('Email')
                send_mail(mail_subject, message, ['oda.group9@gmail.com'], [to_email])
                return render(request, 'Registration/password_reset_done.html', {})
            else:
                return HttpResponse('Email does not exist')
        else:
            return HttpResponse('Please enter a valid email')
    else:
        form = PasswordResetForm()
        return render(request, 'Registration/password_reset_form.html', {'form': form})


def user_password_reset(request, uidb64, token):
    if request.method == 'POST':
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            password1 = form.cleaned_data.get('Password')
            password2 = form.cleaned_data.get('Confirm_Password')
            if password1 == password2:
                try:
                    uid = urlsafe_base64_decode(uidb64).decode()
                    user = User.objects.get(pk=uid)
                except(TypeError, ValueError, OverflowError, User.DoesNotExist):
                    user = None
                if user is not None and password_reset_token.check_token(user, token):
                    user.set_password(password1)
                    user.save()
                    return render(request,'Registration/password_reset_complete.html')
                else:
                    return HttpResponse('Invalid reset link')
            else:
                return HttpResponse('Password does not match')
        else:
            return render(request, 'Registration/password_reset_confirm.html', {'form': form})
    else:
        form = SetNewPasswordForm()
        return render(request, 'Registration/password_reset_confirm.html', {'form': form})


@login_required
def upload(request):

    if "GET" == request.method:
        return render(request, 'Registration/upload.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        name= str(excel_file)[-4:]
        print(name)
        # you may put validations here to check extension or file size
        if name == 'xlsx':
            wb = openpyxl.load_workbook(excel_file)

            worksheet = wb["Sheet1"]

            excel_data = list()

            for row in worksheet.iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(str(cell.value))
                excel_data.append(row_data)
            print(excel_data)
            med_shop = Medical_shop.objects.create(shop_id=request.POST['sid'], shop_name=request.POST['sname'],Lattitude=request.POST['lat'] , Longitude=request.POST['log'])
            for i in excel_data:
                medi= i[0]
                stk= i[1]
                print(medi)
                stock= Stock_availability.objects.create(Medicine_name=medi, Stock=stk ,shop_id=med_shop )

            return render(request ,"Registration/home.html")
        else:
            return HttpResponse("This is not an EXCEL file ......PLEASE choose a valid file")

def reset(request):
    return render(request , "Registration/password_reset_form.html")
