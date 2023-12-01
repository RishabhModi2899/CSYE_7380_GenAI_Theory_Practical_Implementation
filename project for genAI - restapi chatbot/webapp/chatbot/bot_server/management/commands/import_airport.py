import csv
from django.core.management.base import BaseCommand
from bot_server.models import Airport


class Command(BaseCommand):
    help = 'Import airports from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The CSV file to import')

    def handle(self, *args, **options):
        with open(options['csv_file'], mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Handle empty strings for float fields
                latitude = row['LATITUDE']
                longitude = row['LONGITUDE']
                latitude = float(latitude) if latitude else None
                longitude = float(longitude) if longitude else None

                Airport.objects.update_or_create(
                    iata_code=row['IATA_CODE'],
                    defaults={
                        'airport': row['AIRPORT'],
                        'city': row['CITY'],
                        'state': row['STATE'],
                        'country': row['COUNTRY'],
                        'latitude': latitude,
                        'longitude': longitude
                    }
                )
        self.stdout.write(self.style.SUCCESS(
            'Airport data imported successfully'))
