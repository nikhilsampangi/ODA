from django import forms
from django.contrib.auth.models import User


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        help_texts = {
            'username': None,
            'password': None,
         }

class PasswordResetForm(forms.Form):
    Email = forms.EmailField(label='Email',help_text="Please enter the email with which you have registered.")
    fields = ('Email')


class SetNewPasswordForm(forms.Form):
    Password = forms.CharField(widget=forms.PasswordInput())
    Confirm_Password = forms.CharField(widget=forms.PasswordInput())
