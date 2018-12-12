from django.urls import path, include
from . import views



urlpatterns = [
    path('', views.home_page, name='pat_home_page'),
    path('mail/<lat>/<long>', views.mail, name='mail'),
    path('doctors', views.doctor_list, name='doctor_list_page'),
    path('doctor_locator', views.doctor_locator, name='doctor_locator'),
    path('appointments', views.my_appointments, name='my_appointments'),
    path('blood_banks', views.blood_bank, name='blood_banks'),
    path('pharma_locator', views.pharma_locator, name='pharma_loc'),
    path('general_medicines', views.gen_meds, name='gen_meds'),
    path('api/bloodbank', views.Bloodbanklistview.as_view(), name='bloodbank'),
    path('api/medicalshop', views.Medicalshoplistview.as_view(), name='medicalshop'),
    path('avail/<shop_name>/', views.avail, name='avail'),
    path('bloodavail/<bank_name>/', views.bloodavail, name='bloodavail'),
    path('getlocation/', views.getlocation, name='location'),
    path('profile/',views.ProfileUpadate,name='profile-upadate'),
    path('DandS/',include('DandS.urls')),
    path('take_appointment',views.take_appo, name='take_appo'),
    path('booked',views.book, name='book'),
    path('appo/<doctor>/', views.appo, name='avail'),
    path('appo/<doc>/booked', views.booked, name='avail'),
    path('stock_availability', views.pharma_stock, name='pharma_stock'),
    path('about_us', views.about, name='about_page'),
    path('doctor_search', views.doc_ident,name='doctor_identification'),
    path('doc', views.doc,name='doc'),
    path('faq', views.faq,name='faq'),
]
