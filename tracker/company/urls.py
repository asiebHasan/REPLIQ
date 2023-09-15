from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.company_registration, name='company-registration'),
    path('login/', views.company_login, name='company-login')
]
