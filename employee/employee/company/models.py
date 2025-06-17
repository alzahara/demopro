from django.db import models

class employee(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.IntegerField()
    Salary=models.IntegerField()
    Designation=models.CharField(max_length=100)
    Place=models.CharField(max_length=100)
    image=models.ImageField(upload_to="employees")
    Department=models.CharField(max_length=100)
