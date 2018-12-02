from django.contrib import messages
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
                messages.info(request,
                              f'You are already logged in as patient!, Log out to login from different account') ##add in html
                raise redirect('pat_home_page')
        else:
            messages.info(request, f'You are have to login to access respective person')     ##add in html
            return redirect('frontpage')
    return login
