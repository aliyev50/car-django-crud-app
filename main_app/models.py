from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=2083)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.year} {self.brand} {self.model} - ${self.price}"
    
    def get_absolute_url(self):
        return reverse('car-detail', kwargs={'car_id': self.id})
    
    
class CartItem(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return (f'{self.quantity} x {self.car.year} {self.car.brand} {self.car.model} '
        f'- ${self.car.price} - {self.car.description} - {self.car.image}')
        
        
        
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} favorited {self.car.brand} {self.car.model}'