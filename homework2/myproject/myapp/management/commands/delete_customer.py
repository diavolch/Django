from django.core.management.base import BaseCommand
from myapp.models import Customer


class Command(BaseCommand):
    help = 'Delete customer by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Customer id')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        customer = Customer.objects.filter(pk=pk).first()
        customer.delete()
        self.stdout.write(f'Customer: {customer}')