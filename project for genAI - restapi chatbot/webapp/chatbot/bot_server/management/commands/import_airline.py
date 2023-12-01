import csv
from django.core.management.base import BaseCommand
from bot_server.models import Airline


class Command(BaseCommand):
    help = 'Import airlines from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The CSV file to import')

    def handle(self, *args, **options):
        with open(options['csv_file'], mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Airline.objects.update_or_create(
                    iata_code=row['IATA_CODE'],
                    defaults={'airline': row['AIRLINE']}
                )
        self.stdout.write(self.style.SUCCESS(
            'Airline data imported successfully'))
