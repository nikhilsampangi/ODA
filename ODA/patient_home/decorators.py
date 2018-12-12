from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect


def only_patient(func):
    def login(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                if request.user.patient_db.user_pat == 'yes':
                   return func(request, *args, **kwargs)
                elif request.user.patient_db.user_pat == 'no':
                    return redirect('welcome:pat_log')
                else:
                    raise PermissionDenied
            except:
                pass
            try:
               if request.user.doctors.user_pat == 'no':
                   return redirect('welcome:home')
               else:
                   raise PermissionDenied
            except:

                pass

        else:
            messages.info(request, f'You are have to login to access respective person')     ##add in html
            return redirect('welcome:frontpage')
    return login
