from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from welcome.models import Doctors

class User_update_Form(forms.ModelForm):

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={})
        }
        fields = ('username', )


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ('Phone','Desc','doc_type','Degrees','d_website','About_Clinic','Other_info')
