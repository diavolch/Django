from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import Order, Product, Customer


class Command(BaseCommand):
    help = "Create order"
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('id_customer', type=int, help='Id customer')

    def handle(self, *args, **kwargs):
        customer = Customer.objects.filter(pk=2).first()
        p1 = Product.objects.filter(pk=1).first()
        p2 = Product.objects.filter(pk=2).first()
        p3 = Product.objects.filter(pk=3).first()
        order = Order(customer=customer, total_price=0)
        order.save()
        order.product.add(p1,p2,p3)
        self.stdout.write(f'Customer: {customer.name}')
