from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.about, name='index'),
    url(r'^about/$', views.about, name ='about'),
]