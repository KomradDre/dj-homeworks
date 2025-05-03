import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify


class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                price=float(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'].lower() == 'true',
                slug=slugify(phone['name'])
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully imported {len(phones)} phones'))