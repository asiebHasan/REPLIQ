from django.contrib import admin
from .models import Company
# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'email','is_active','is_staff']
    search_fields = ['company_name']