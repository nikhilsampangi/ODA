from django.conf.urls import url
from  . import views

urlpatterns = [
    url(r'^$',views.linking, name='linking'),
    url(r'^search/$',views.search,name="search"),
    url(r'^(?P<body_part>[A-z]+)/$',views.index, name='index'),
    url(r'^(?P<body_part>[A-z]+)/(?P<d_name>[A-z]+)/$', views.info, name='info'),
]