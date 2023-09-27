from django.core.management.base import BaseCommand
from myapp.models import Product


class Command(BaseCommand):
    help = 'Update Product by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Product id')
        parser.add_argument('title', type=str, help='Product title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = Product.objects.filter(pk=pk).first()
        product.title = kwargs.get('title')
        product.save()
        self.stdout.write(f'Product: {product}')