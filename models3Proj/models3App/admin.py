from django.contrib import admin
from .models import Book
from .models import Car



# Register your models here.

# TO REGISTER MODELS ONTO SITE
admin.site.register(Book)
admin.site.register(Car)