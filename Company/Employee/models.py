from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField()
    designation = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to="employee")
    department_name = models.CharField(max_length=50)

