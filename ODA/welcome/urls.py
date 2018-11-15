from django.urls import path
from . import views


urlpatterns=[
    path('',views.front_page),
    path('doctor/',views.doctor_page),
]
