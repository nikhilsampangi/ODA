from django.urls import path
from django.views.generic.base import TemplateView
from Registration import views
app_name = 'Registration'

urlpatterns = [
    # path('',TemplateView.as_view(template_name='Registration/home.html'), name='pharmacies'),
    path('',views.homepage, name='pharmacies'),
    path('signup/', views.register, name='signup'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('userlogout/',views.userlogout,name='userlogout'),
    #path('data/', views.data, name="data"),
    path('upload/',views.upload, name='upload'),
    #path('data1/',views.data1 , name='data1'),
    path('reset/',views.reset,name='reset'),
]
