from django.core.management.base import BaseCommand
from myapp.models import Customer


class Command(BaseCommand):
    help = "Create customer"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Create fake customers')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count):
            customer = Customer(name=f'Name{i}', email=f'mail{i}@example.com',
                            phone=f'+799900000{i}', address=f'Somewhere{i}')
            customer.save()
        # self.stdout.write(f'{customer}')
