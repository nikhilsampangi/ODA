from django.urls import path
from . import views


urlpatterns=[
    path('',views.home_page, name='pat_home_page'),
    path('doctors', views.doctor_list, name='doctor_list_page'),
    path('doctor_locator',views.doctor_locator, name='doctor_locator'),
    path('appointments',views.my_appointments, name='my_appointments'),
    path('blood',views.blood_bank),
]
