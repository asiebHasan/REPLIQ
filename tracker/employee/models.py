from django.db import models
from company.models import Company

# Create your models here.
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    employee_id = models.CharField(max_length=20)
    contact_email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"