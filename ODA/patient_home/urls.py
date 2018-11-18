from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='pat_home_page'),
    path('doctors', views.doctor_list, name='doctor_list_page'),
    path('doctor_locator', views.doctor_locator, name='doctor_locator'),
    path('appointments', views.my_appointments, name='my_appointments'),
    path('blood_banks', views.blood_bank, name='blood_banks'),
    path('pharma_locator', views.pharma_locator, name='pharma_loc'),
    path('general_medicines', views.gen_meds, name='gen_meds'),
]
