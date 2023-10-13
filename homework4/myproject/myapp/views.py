from datetime import timedelta

from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.datetime_safe import datetime

from .forms import CustomerForm, ProductForm, ImageForm
from .models import Customer, Product, Order


def index(request):
    return render(request, 'base.html')


def get_all_customers(request):
    context = 'Customers'
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'context': context, 'customers': customers})


def get_all_products(request):
    context = 'Products'
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


def create_customer(request):
    context = 'Создание клиента'
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = Customer(name=form.cleaned_data['name'],
                                email=form.cleaned_data['email'],
                                phone=form.cleaned_data['phone'],
                                address=form.cleaned_data['address']
                                )
            customer.save()
            messages.add_message(request, messages.SUCCESS, 'Успешно')
    else:
        form = CustomerForm()
    return TemplateResponse(request, 'templates_form.html', {"form": form, 'context': context})


def create_product(request):
    context = 'Создание товара'
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data['img']
            fs = FileSystemStorage()
            fs.save(img.name, img)
            product = Product(title=form.cleaned_data['title'],
                              description=form.cleaned_data['description'],
                              price=form.cleaned_data['price'],
                              count=form.cleaned_data['count'],
                              img=img.name
                              )
            product.save()
            messages.add_message(request, messages.SUCCESS, 'Успешно')
    else:
        form = ProductForm()
    return TemplateResponse(request, 'templates_form.html', {"form": form, 'context': context})


def get_all_products(request):
    context = 'Список товаров'
    products = Product.objects.all()
    return TemplateResponse(request, 'products.html', {'context': context, 'products': products})
