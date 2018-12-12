from django import forms
from blog.models import textinblog


class Bloginput(forms.ModelForm):
    # the_text = forms.Textarea()
    # the_sub = forms.CharField(max_length=150)
    # picture = forms.ImageField()
    class Meta:
        model = textinblog
        fields = ['the_text', 'the_sub', 'picture']
