from django.core.management.base import BaseCommand
from myapp.models import Customer


class Command(BaseCommand):
    help = "Create customer"

    def handle(self, *args, **kwargs):
        customer = Customer(name='Leo', email='leo@example.com',
                            phone='+7999000000', address='Somewhere')
        customer.save()
        self.stdout.write(f'{customer}')
