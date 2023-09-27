from datetime import timedelta

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datetime_safe import datetime

from .models import Customer, Product, Order


def index(request):
    return HttpResponse('Главная страница')


def get_all_customers(request):
    context = {'customers': 'Customers'}
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'context': context, 'customers': customers})


def get_all_products(request):
    context = {'products': 'Products'}
    products = Product.objects.all()
    return render(request, 'products.html', {'context': context, 'products': products})


def get_orders(request, customer_id, days):
    context = {'orders': 'Orders'}
    products = []
    now = datetime.now()
    before = now - timedelta(days=days)
    customer = Customer.objects.filter(pk=customer_id).first()
    orders = Order.objects.filter(customer=customer, date_ordered__range=(before, now)).all()
    for order in orders:
        products.append(order.product.all())
    products.reverse()
    return render(request, 'orders.html', {'context': context, 'customer': customer.name, 'products': products})