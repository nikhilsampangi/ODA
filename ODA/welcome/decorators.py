from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.http import HttpResponse


def only_doctor(func):
    def login(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.doctors.user_pat == 'no':
                   return func(request, *args, **kwargs)
            except:
                raise PermissionDenied
        else:
            return redirect('welcome:frontpage')
    return login

def user_not_auth(func):
    def not_log(request, *args, **kwargs):
        if request.user.is_authenticated is False:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('First logout to login again')
    return not_log

