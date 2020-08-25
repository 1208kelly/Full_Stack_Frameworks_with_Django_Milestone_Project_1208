from django.shortcuts import render

# Create your views here.

def shop(request):
	context = {}
	return render(request, 'shop/shop.html', context)

def shopping_cart(request):
	context = {}
	return render(request, 'shop/shopping_cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'shop/checkout.html', context)