from django.urls import path
from . import views

urlpatterns = [


    path('every/', views.login_every, name='Login_every'),
    path('doc/', views.login_doc, name='Login_doc'),


]
