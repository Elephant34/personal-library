from django.db import models
from django.contrib.auth import get_user_model

ratings_list = (
        (0,"0"),
        (1,"1 Star"),
        (2,"2 Stars"),
        (3,"3 Stars"),
        (4,"4 Stars"),
        (5,"5 Stars!"),
    )

# Create your models here.
class Book(models.Model):
    '''
    Database to catalogue books
    '''
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    series = models.CharField(default=None, max_length=256)
    rating = models.IntegerField(choices=ratings_list)
    last_read = models.DateField()

    def __str__(self):
        return self.title

class Recipe(models.Model):
    '''
    Database to catalogue recipies
    '''
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    source = models.CharField(max_length=256)
    food_type = models.CharField(default=None, max_length=256)
    rating = models.IntegerField(choices=ratings_list)
    last_made = models.DateField()

    def __str__(self):
        return self.title
