from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.car_index, name='car-index'),
    path('cars/<int:car_id>/', views.car_detail, name='car-detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car-create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car-update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car-delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:car_id>/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.view_cart, name='checkout'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-favorites/<int:car_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('favorites/', views.view_favorites, name='view_favorites'),
    path('remove-from-favorites/<int:favorite_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
