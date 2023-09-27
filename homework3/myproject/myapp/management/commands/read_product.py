from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Find product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='product id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        self.stdout.write(f'Product: {product}')