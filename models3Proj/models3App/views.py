from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Car



# Create your views here.
def index(request):
    return HttpResponse("test")


# FUNCTION TO CREATE NEW BOOK
def newBook(request):
    createBook = Book(name ="Tulips", pageNumber= 150, genre="Poetry", publishDate = '2018-02-04')
    createBook.save()
    return HttpResponse(str(createBook.name) + " " + str(createBook.pageNumber) + " " + str(createBook.genre) + " " + str(createBook.publishDate))


# FUNCTION TO SEE ALL BOOKS IN ARRAY
def allBooks(request):
    seeAll = Book.objects.all()
    return HttpResponse(seeAll)

# FUNCTION TO CREATE NEW CAR OBJECT
def newCar(request):
    driveThis = Car(make = "Audi", model="800", year=2017)
    driveThis.save()
    return HttpResponse(str(driveThis.make) + "" + str(driveThis.model) + "" + str(driveThis.year))

def allCars(request):
    allCars = Car.objects.all()
    return HttpResponse(allCars)