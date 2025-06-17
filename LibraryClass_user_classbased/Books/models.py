from django.db import models

# Create your models here.

#Model Definition(database schema)
class Book(models.Model):
     title = models.CharField(max_length=100)
     author = models.CharField(max_length=100)
     price = models.IntegerField()
     language = models.CharField(max_length=100)
     pages = models.IntegerField()
     image=models.ImageField(upload_to="books")

