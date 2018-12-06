from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
# from patient_home import views

app_name = 'welcome'

urlpatterns = [

    path('doc_home/', views.home, name='home',),
    path('', views.front_page, name='frontpage'),
    path('logout/', auth_views.LogoutView.as_view(template_name='welcome/home.html'), name='logout'),
    path('doctor/', views.doctor_page, name='doc-l-r'),
    path('doc_login/', views.doc_login, name='doc-login'),
    path('doc_register/', views.doc_register, name='doc-register'),
    path('user_register/', views.pat_log, name='pat_log'),

]
