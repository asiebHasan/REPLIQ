from django.urls import path
from  . import views

urlpatterns = [
     path('add/', views.add_employee, name='add-employee'),
     path('list/', views.employee_list, name='employee-list'),
]
