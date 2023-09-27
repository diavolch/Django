from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=150)
    date_of_registered = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.name} {self.email}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default='None')
    price = models.DecimalField(max_digits=9, decimal_places=2)
    count = models.IntegerField(default=0)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Title: {self.title}, price: {self.price}'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField("Product")
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer}, product: {self.product}, time: {self.date_ordered}, total_price: {self.total_price}'

