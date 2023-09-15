from django.contrib import admin
from .models import Device, DeviceLog

# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['serial_number','name','description', 'condition',]
    list_filter = ['condition',]
    search_fields = ['serial_number','name',]

@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = ['device', 'employee', 'condition', 'checked_out_date','returned_date','returned_condition']
    list_filter = ['device', 'employee','checked_out_date','returned_date']
    search_fields = ['device', 'employee']