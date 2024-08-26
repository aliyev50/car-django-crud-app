from django.db import models
from django.urls import reverse

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=2083)
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - ${self.price}"
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})