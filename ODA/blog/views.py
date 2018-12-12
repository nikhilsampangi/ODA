from django.shortcuts import render, redirect
from blog.forms import Bloginput
from blog.models import textinblog, Doctors
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    spec = Doctors.objects.get(D_Id=request.user).Spec.split()
    author = Doctors.objects.get(D_Id=request.user).D_Id
    return render(request, 'blog/blogpage.html', {'posts': textinblog.objects.all(), 'spec': spec, 'author': author})


@login_required
def make(request):
    if request.method == 'POST':
        blotext = Bloginput(request.POST, request.FILES)

        if blotext.is_valid():
            subj = blotext.cleaned_data['the_sub']
            blotext.save(commit=False)
            user = Doctors.objects.get(D_Id=request.user)
            text = blotext.cleaned_data['the_text']
            picture = blotext.cleaned_data['picture']
            b = textinblog(doctors=user, the_text=text, the_sub=subj, picture=picture)
            b.save()
            return redirect('blog:blog_home')
    else:
        blotext = Bloginput()
        return render(request, 'blog/make.html', {'form': blotext})


def edit(request, post_id):
    textinblog.objects.get(id=post_id).delete()
    if request.method == 'POST':
        blotext = Bloginput(request.POST, request.FILES)
        if blotext.is_valid():
            subj = blotext.cleaned_data['the_sub']
            blotext.save(commit=False)
            user = Doctors.objects.get(D_Id=request.user)
            text = blotext.cleaned_data['the_text']
            picture = blotext.cleaned_data['picture']
            b = textinblog(doctors=user, the_text=text, the_sub=subj, picture=picture)
            b.save()
            return redirect('blog:blog_home')
    else:
        blotext = Bloginput()
    return render(request, 'blog/make.html', {'form': blotext})


def de1(request, post_id):
    textinblog.objects.get(id=post_id).delete()
    return redirect('blog:blog_home')
