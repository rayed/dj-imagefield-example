from django.conf.urls import patterns, url

from gallery import views

urlpatterns = patterns('',
  url(r'^$', views.index, name='home'),
  url(r'^new/$', views.image_create, name='image_new'),
  url(r'^edit/(?P<pk>\d+)$', views.image_update, name='image_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.image_delete, name='image_delete'),
)