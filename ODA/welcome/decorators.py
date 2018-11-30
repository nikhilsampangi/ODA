from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def only_doctor(func):
    def login(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.doctors.user_pat == 'no':
                   return func(request, *args, **kwargs)
            except:
                raise PermissionDenied

    return login
