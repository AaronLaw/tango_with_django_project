from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/add$', views.add_category, name='add_category'), # Notice: this rule should be placed before P<category_name_slug>
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', 
    	views.show_category, name='show_category'),
    url(r'^about/$', views.about, name ='about'),
]