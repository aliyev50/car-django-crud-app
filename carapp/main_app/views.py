from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car



class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    uccess_url = '/cars/'
     
     
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

def home(request):
    return render(request, 'home.html')

def car_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def about(request):
    return render(request, 'about.html')

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})


