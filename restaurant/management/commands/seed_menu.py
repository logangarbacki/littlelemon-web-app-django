from django.core.management.base import BaseCommand
from django.core.management import call_command
from restaurant.models import MenuItem


class Command(BaseCommand):
    help = 'Seeds menu items from fixture if the table is empty'

    def handle(self, *args, **kwargs):
        if MenuItem.objects.exists():
            self.stdout.write('Menu already has items — skipping seed.')
            return
        call_command('loaddata', 'restaurant/fixtures/menu.json')
        self.stdout.write(self.style.SUCCESS(f'Seeded {MenuItem.objects.count()} menu items.'))
