from django.contrib import admin
from .models import Book, Recipe

# Register your models here.
admin.site.register(Book)
admin.site.register(Recipe)