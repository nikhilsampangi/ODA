from django.urls import path

from Registration import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]