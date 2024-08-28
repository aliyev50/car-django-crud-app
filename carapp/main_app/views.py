from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Car, CartItem, Favorite
from django.contrib import messages 
 



class CarCreate(CreateView):
    model = Car
    fields = '__all__'
    uccess_url = '/cars/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.car.price * item.quantity for item in cart_items)
    return render(request, 'main_app/cart.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, car_id):
    car = Car.objects.get(id=car_id)
    cart_item, created = CartItem.objects.get_or_create(car=car, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('view_cart')
     

  
class CarUpdate(UpdateView):
    model = Car
    fields = '__all__'


class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'
    
class Home(LoginView):
    template_name = 'home.html'

def home(request):
    return render(request, 'home.html')

@login_required
def car_index(request):
    cars = Car.objects.filter(user=request.user)
    return render(request, 'cars/index.html', {'cars': cars})

def about(request):
    return render(request, 'about.html')

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'cars/detail.html', {'car': car})


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

def add_to_favorites(request, car_id):
    car = Car.objects.get(id=car_id)
    favorite, created = Favorite.objects.get_or_create(car=car, user=request.user)
    
    if created:
        # Optionally, you could add a success message here.
        print(f"Added {car} to favorites.")
    
    return redirect('view_favorites')


def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'main_app/favorites.html', {'favorites': favorites})

def remove_from_favorites(request, favorite_id):
    try:
        favorite = Favorite.objects.get(id=favorite_id, user=request.user)
        favorite.delete()
        messages.success(request, "The car was successfully removed from your favorites.")
    except Favorite.DoesNotExist:
        messages.error(request, "The car could not be found in your favorites.")
    
    return redirect('view_favorites')