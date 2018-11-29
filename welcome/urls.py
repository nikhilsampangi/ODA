from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'welcome'

urlpatterns=[
    path('home/',views.home,name='home'),
    path('patient_reg/', views.patient_reg, name='val-user'),
    path('',views.front_page,name='frontpage'),
    path('logout/',auth_views.LogoutView.as_view(template_name='welcome/logout.html'),name='logout'),
    path('doctor/',views.doctor_page ,name='doc-l-r'),
    path('doc_login/', views.doc_login, name='doc-login'),
    path('doc_register/', views.doc_register, name='doc-register'),
    path('val_user/', views.val_user, name='pat-register'),
    path('pat_log/', views.patient_log, name='pat-login'),

]
