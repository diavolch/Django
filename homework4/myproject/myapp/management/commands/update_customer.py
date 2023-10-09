from django.core.management.base import BaseCommand
from myapp.models import Customer


class Command(BaseCommand):
    help = 'Update customer by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer id')
        parser.add_argument('name', type=str, help='Customer name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        customer.name = kwargs.get('name')
        customer.save()
        self.stdout.write(f'Customer: {customer}')