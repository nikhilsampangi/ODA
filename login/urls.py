from django.urls import path
from . import views

urlpatterns = [


    path('every/', views.login_every, name='Login_every'),
    path('doc/', views.login_doc, name= 'login_doc'),
    path('everyone/',views.cred_every, name ="cred_every"),
    path('doctor/',views.cred_doc, name ="cred_doctor"),


]
