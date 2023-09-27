from django.core.management.base import BaseCommand
from django.utils import timezone
from myapp.models import Product, Customer


class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('id_customer', type=int, help='Id customer')
        parser.add_argument('id_product', type=int, help='Id product')

    def handle(self, *args, **kwargs):
        id_customer = kwargs.get('id_customer')
        id_product = kwargs.get('id_product')
        customer = Customer.objects.filter(pk=id_customer).first()
        product = Product.objects.filter(pk=id_product).first()
        # products.html = []
        # for i in id_products:
        #     product = Product.objects.filter(pk=i).first()
        #     products.html.append(product)
        customer.orders.set([product])

        self.stdout.write(f'Customer: {customer.name}, product: {product.title}')