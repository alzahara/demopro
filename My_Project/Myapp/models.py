from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=50)
    password =models.IntegerField()
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    image = models.ImageField(upload_to="person")
    address = models.CharField(max_length=50)
