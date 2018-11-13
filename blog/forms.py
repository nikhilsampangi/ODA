from django import forms
from blog.models import textinblog


class Bloginput(forms.ModelForm):
    class Meta:
        model = textinblog
        fields = ['the_text']
