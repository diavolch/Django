from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Delete product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        product.delete()
        self.stdout.write(f'Product: {product}')