from django.conf.urls import url
from  . import views

urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^(?P<d_name>[A-z]+)/$',views.info ,name='info'),

]