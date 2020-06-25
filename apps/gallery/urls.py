from django.urls import path

from . import views

app_name = 'gallery'

urlpatterns = [
  path('', views.index, name='home'),
  path('new/', views.image_create, name='image_new'),
  path('edit/<int:pk>/', views.image_update, name='image_edit'),
  path('delete/<int:pk>/', views.image_delete, name='image_delete'),
]