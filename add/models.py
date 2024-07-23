from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    emp_id = models.UUIDField()
    salary = models.IntegerField()
    description = models.TextField()
    joining_date = models.DateField(auto_now_add=True)
    applied_for_resignation = models.BooleanField(default=False)