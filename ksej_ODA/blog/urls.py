from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('make/', views.make, name='make_blog'),
]
