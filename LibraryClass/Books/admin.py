from django.contrib import admin

# Register your models here.
from Books.models import Book
admin.site.register(Book)