from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from welcome.models import Patient_DB

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Patient_DB
        fields = ('emerg_email','Blood_group','Phone_num','Emergency_num','medical_con')

