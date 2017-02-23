from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/create/$', views.create_category, name='create_category'), # Notice: this rule should be placed before P<category_name_slug>
    url(r'^category/show/(?P<category_name_slug>[\w\-]+)/$', 
    	views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/page/create/$', views.create_page, name='create_page'),
    url(r'^about/$', views.about, name ='about'),
    url(r'^register/$', views.register, name = 'register'),
]