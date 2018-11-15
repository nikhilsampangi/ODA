from django.shortcuts import render, redirect
from blog.forms import Bloginput
from blog.models import textinblog, Doctors
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    spec = Doctors.objects.get(D_Id=request.user).T_Id.Spec.split()
    return render(request, 'blog/blogpage.html', {'posts': textinblog.objects.all(), 'spec': spec})


@login_required
def make(request):
    if request.method == 'POST':
        blotext = Bloginput(request.POST)

        if blotext.is_valid():
            subj = blotext.cleaned_data['the_sub']
            blotext.save(commit=False)
            user = Doctors.objects.get(D_Id=request.user)
            text = blotext.cleaned_data['the_text']
            b = textinblog(doctors=user, the_text=text, the_sub=subj)
            b.save()
            return redirect('blog_home')
    else:
        blotext = Bloginput()
    return render(request, 'blog/make.html', {'form': blotext})
