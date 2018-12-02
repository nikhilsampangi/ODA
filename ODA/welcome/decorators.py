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
            except Exception as ex:

                raise PermissionDenied
        else:
            messages.info(request, f'You are have to login to access respective person')     ##add in html
            return redirect('frontpage')
    return login

def user_not_auth(func):
    def not_log(request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return func(request, *args, **kwargs)
        else:
            # messages.success(request, f'First logout to login again again')
            return HttpResponse('<h1> Permission Denied <br><br></h1><h2> Logout visit the page </h2>')
    return not_log

