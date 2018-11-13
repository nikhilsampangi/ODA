from django.shortcuts import render, redirect
from blog.forms import Bloginput
from blog.models import textinblog, Doctors


def home(request):
    return render(request, 'blog/blogpage.html', {'posts': textinblog.objects.all()})


def make(request):
    if request.method == 'POST':
        blotext = Bloginput(request.POST)

        if blotext.is_valid():
            # Subject get here
            blotext.save(commit=False)
            user = Doctors.objects.get(D_Id=request.user)
            text = blotext.cleaned_data['the_text']
            b = textinblog(doctors=user, the_text=text)
            b.save()
            return redirect('blog_home')
    else:
        blotext = Bloginput()
    return render(request, 'blog/make.html', {'form': blotext})
