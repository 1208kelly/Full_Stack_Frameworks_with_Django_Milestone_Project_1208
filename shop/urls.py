from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('shoppingcart/', views.shopping_cart, name="shopping cart"),
    path('checkout/', views.checkout, name="checkout")
]
