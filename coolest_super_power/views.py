from django.shortcuts import render

def store(request):
	context = {}
	return render(request, 'coolest_super_power/store.html', context)

def shopping_cart(request):
	context = {}
	return render(request, 'coolest_super_power/shopping_cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'coolest_super_power/checkout.html', context)