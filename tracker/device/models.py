from django.db import models
from company.models import Company
from employee.models import Employee

# Create your models here.
class Device(models.Model):
    serial_number = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(max_length=20)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    checked_out_date = models.DateTimeField(auto_now=True)
    returned_condition = models.CharField(max_length=255, blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.employee} borrowed {self.device}'
    