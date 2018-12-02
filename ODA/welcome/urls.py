from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
# from patient_home import views


urlpatterns = [
    path('doc_home/', views.home, name='home',),
    path('', views.front_page, name='frontpage'),
    path('logout/', auth_views.LogoutView.as_view(template_name='welcome/home.html'), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('doctor/', views.doctor_page, name='doc-l-r'),
    path('doc_login/', views.doc_login, name='doc-login'),
    path('doc_register/', views.doc_register, name='doc-register'),
    path('user_register/', views.pat_log, name='pat_log'),

 ### Paths for the password reset
    path('Password-Reset/', auth_views.PasswordResetView.as_view(template_name='welcome/password_reset.html'),
         name='password_reset'),
    path('Password-Reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='welcome/password_reset_done.html'),
         name='password_reset_done'),
    path('Password-Reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='welcome/password_reset_con.html'),
         name='password_reset_confirm'),
    path('Password-Reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='welcome/pass_reset_complete.html'),
         name='password_reset_complete'),
]
