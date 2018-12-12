from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponse


def only_doctor(func):
    def login(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.doctors.user_pat == 'no':
                   return func(request, *args, **kwargs)
                else:
                    raise PermissionDenied
            except:
                print('this isn')
                print(request.user.doctors.user_pat)
                pass
            try:
               if request.user.patient_db.user_pat == 'yes':
                   return redirect('pat_home_page')
               else:
                   raise PermissionDenied
            except:
                pass
        else:
            messages.info(request, f'You are have to login to access respective person')     ##add in html
            return redirect('welcome:frontpage')
    return login

def user_not_auth(func):
    def not_log(request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return func(request, *args, **kwargs)
        else:
            try:
                if request.user.doctors.user_pat == 'no':
                   return redirect('welcome:home')
                else:
                    raise PermissionDenied
            except:
                pass
            try:
               if request.user.patient_db.user_pat == 'yes':
                   return redirect('pat_home_page')
               elif request.user.patient_db.user_pat == 'no':
                   return redirect('welcome:logout')
            except:
                pass
            # return HttpResponse('<h1> Permission Denied <br><br></h1><h2> Logout visit the page </h2>')
    return not_log
