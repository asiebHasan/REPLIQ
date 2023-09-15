from django.contrib import admin
from .models import Employee


# Register your models here.
@admin.register(Employee)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['employee_id','first_name', 'last_name','contact_email','company']
    search_fields = ['employee_id','first_name', 'last_name']