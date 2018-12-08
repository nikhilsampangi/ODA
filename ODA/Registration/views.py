import openpyxl as openpyxl
import required as required
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import Medical
# Create your views here.
from Registration.forms import UserInfoForm

"""
class SignUp(generic.CreateView):

    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    #template_name = 'signup.html'
"""
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

@login_required
def data(request):
    return render(request,'Registration/shop_data.html')

@login_required
def data1(request):
    #print("Request Object: {}".format(request.POST))
    Shop_id=request.POST['sid']
    Shop_name=request.POST['sname']
    lattitude=request.POST['lati']
    longitude=request.POST['longi']
    med_shop=Medical.objects.create(shop_id=Shop_id,shop_name=Shop_name,Lattitude=lattitude,Longitude=longitude)
    return HttpResponse("data entered succesfully")

@login_required
def upload(request):
    if "GET" == request.method:
        return render(request, 'Registration/upload.html', {})
    else:
        excel_file = request.FILES["excel_file"]
        print(excel_file)
        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting all sheets
        #sheets = wb.sheetnames
        #print(sheets)

        # getting a particular sheet
        worksheet = wb["Sheet1"]
        #print(worksheet)

        # getting active sheet
        #active_sheet = wb.active
        #print(active_sheet)

        # reading a cell
        #print(worksheet["A1"].value)

        excel_data = list()
        # iterating over the rows and getting value from each cell in row

        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)
        print(excel_data)

        return HttpResponse("Uploaded succesfully")