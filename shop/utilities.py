import json
from .models import *


def cookieShoppingCart(request):
    try:
        shoppingCart = json.loads(request.COOKIES['shoppingCart'])
    except:
        shoppingCart = {}

    print('ShoppingCart', shoppingCart)
    items = []
    order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
    cartItems = order['get_cart_items']

    for i in shoppingCart:
        # using try to stop any items in shopping cart that were removed from causing an error
        try:
            cartItems += shoppingCart[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * shoppingCart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += shoppingCart[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                    },
                'quantity': shoppingCart[i]['quantity'],
                'get_total': total,
                }
            items.append(item)
            # if item is not digital, change order shipping value to true
            if product.digital == False:
                order['shipping'] = True
        except:
            pass

    return {'cartItems': cartItems, 'order': order, 'items': items}


def shoppingCartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # get or create from stack overflow and djangoproject.com
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieShoppingCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestUserOrder(request, data):
    print("User is not signed in")

    print('COOKIES:', request.COOKIES)

    name = data['form']['name']
    email = data['form']['email']
    cookieData = cookieShoppingCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        email = email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer = customer,
        complete = False
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        orderItem = Order.objects.create(
            product = product,
            order = order,
            quantity = item['quantity']
        )
    return customer, order