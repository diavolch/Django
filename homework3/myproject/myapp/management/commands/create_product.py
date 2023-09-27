from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Create fake products.html')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count):
            product = Product(title=f'Title{i}', price=10+i, count=i)
            product.save()

    # def handle(self, *args, **kwargs):
    #     product = Product(title='Title1', price=13.99, count=2)
    #     product.save()
    #     self.stdout.write(f'{product}')
