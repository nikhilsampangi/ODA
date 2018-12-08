from django import forms
from django.contrib.auth.models import User
from welcome.models import Patient_DB


class User_update_Form(forms.ModelForm):
    first_name = forms.CharField(
        label='first_name',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'first_name'}
        )
    )
    last_name = forms.CharField(
        label='last_name',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'last_name'}
        )
    )
    class Meta:
        model = User
        fields = ('first_name','last_name')


class ProfileUpdateForm(forms.ModelForm):
    medical_con = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'medical_con'}
        )
    )
    Emergency_num = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'Emergency_num'}
        )
    )
    Phone_num = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'Phone_num'}
        )
    )
    emerg_email = forms.CharField(
        label='Username',
        max_length=100,
        widget=forms.TextInput(
            attrs={'style':'border-color: #1C7CAC','class': 'w3-input', 'name': 'emerg_email'}
        )
    )
    class Meta:
        model = Patient_DB
        fields = ('emerg_email','Phone_num','Emergency_num','medical_con')

