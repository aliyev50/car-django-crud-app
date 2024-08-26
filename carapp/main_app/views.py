from django.shortcuts import render
from .models import Car



class Car:
    def __init__(self, brand, model, year, price, description, image):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.description = description
        self.image = image
        
cars = [
     Car('Toyota', 'Camry', 2020, 25000, 'A reliable and fuel-efficient sedan.', 'camry2020.jpg'),
]


def home(request):
    return render(request, 'home.html')

# main_app/views.py

def about(request):
    return render(request, 'about.html')

def car_index(request):
    cars = Car.objects.all()  # look familiar?
    return render(request, 'cars/index.html', {'cars': cars})

