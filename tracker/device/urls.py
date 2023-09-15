from django.urls import path
from  . import views

urlpatterns = [
     path('add/', views.add_device, name='add-device'),
     path('list/', views.device_list, name='device-list'),
     path('log/add/', views.add_log, name='add-log'),
     path('log/list/', views.log_list, name='log-list'),
]