from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.


def shop(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/shop.html', context)


def shopping_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # get or create from stack overflow and djangoproject.com
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/shopping_cart.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # get or create from stack overflow and djangoproject.com
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items, 'order': order}
    return render(request, 'shop/checkout.html', context)


def updateItem(request):
    return JsonResponse('Item added', safe=False)