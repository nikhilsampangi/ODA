from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url

urlpatterns = [
    path('nearby', views.nearby,name='nearby'),
    path('current', views.current,name='current'),
    path('first_page', views.first_page,name='first_page'),
    path('tips',views.extratips,name='tips'),
    path('getlocation',views.getlocation,name='getlocation'),
    path('sendingmail',views.sendingmail,name='sendingmail'),
    path('medicalshops',views.medicalshop,name='Medical_shop'),
    path('medicalshops/<shop_name>/',views.shopname,name='Medical_shop_name'),
    path('bloodbanks',views.bloodbank,name='Medical_shop'),
    path('bloodbanks/<bank_name>/',views.bankname,name='Medical_shop_name'),
    path('eye',views.eye,name='eye'),
    path('ear',views.ear,name='ear'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    path('api/bloodlog', views.Bloodbanklistview.as_view(),name='log'),
    path('api/medicallog', views.Medicalshoplistview.as_view(),name='log'),

    ]
urlpatterns+=staticfiles_urlpatterns()
