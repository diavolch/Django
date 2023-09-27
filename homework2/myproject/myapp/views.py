from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datetime_safe import datetime

from .models import Customer, Product


def index(request):
    return HttpResponse('Главная страница')


def get_all_customers(request):
    customers = Customer.objects.all()
    return HttpResponse(customers)


def get_all_products(request):
    products = Product.objects.all()
    return HttpResponse(products)


# def get_all_orders(request):
#     orders = Order.objects.all()
#     return HttpResponse(orders)


def sorted_basket(request, customer_id, days_ago):
    products = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    customer = Customer.objects.filter(pk=customer_id).first()
    orders = customer.orders.all()
    for order in orders:
        products.append(order.products.all())
    products.reverse()
    return render(request, 'orders.html', {'customer': customer, 'orders': orders, 'products.html': products})