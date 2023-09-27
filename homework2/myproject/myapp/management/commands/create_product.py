from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def handle(self, *args, **kwargs):
        product = Product(title='Title1', price=13.99, count=2)
        product.save()
        self.stdout.write(f'{product}')
