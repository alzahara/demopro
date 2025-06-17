from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    description = models.TextField()
    director_name = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    year = models.IntegerField()
    image = models.ImageField(upload_to="movies")
