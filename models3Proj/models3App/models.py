from django.db import models
from django.utils import timezone


# Create your models here.

# BOOK MODEL: pageNum, genre, publishDate
class Book(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100, null=True)
    pageNumber = models.IntegerField(default= 0)
    publishDate = models.DateField(default = timezone.now)

    def __str__(self):
        return self.name



# CAR MODEL: make, model, year
class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(default=0)


    def __str__(self):
        return self.make