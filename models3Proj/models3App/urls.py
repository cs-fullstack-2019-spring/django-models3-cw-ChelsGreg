from django.urls import path
from . import views


# DIRECTING ROUTES TO FUNCTIONS
urlpatterns = [
    path("allCars/", views.allCars, name='allcars'),
    path("newCar/", views.newCar, name='newcar'),
    path("allBooks/", views.allBooks, name='allBooks'),
    path("allBooks/", views.allBooks, name='allBooks'),
    path("newBook/", views.newBook, name='newBook'),
    path("", views.index, name='index'),
]