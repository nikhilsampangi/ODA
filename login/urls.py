from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    path('home/', views.home, name='home-1'),
    path('everyone/', views.login_every, name='Login_every'),
    path('doctor_log/', views.login_doc, name='Login_doc'),
    path('everyone/new_user/',views.new_user,name='new_user'),
    path('everyone/new_user/val_p/',views.val_p,name='val_p'),
    path('doc/', views.cred_doc, name='cred_doc'),
]