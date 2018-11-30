from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def only_patient(func):
    def login(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.patient_db.user_pat == 'yes':
                   return func(request, *args, **kwargs)
                else:
                    raise PermissionDenied
            except:
                raise PermissionDenied

    return login
