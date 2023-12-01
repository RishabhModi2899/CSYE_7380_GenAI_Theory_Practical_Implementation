import csv
from django.core.management.base import BaseCommand
from django.db import transaction
from bot_server.models import Flight
from django.db import models


class Command(BaseCommand):
    help = 'Import the first 1000 rows of flight data from a CSV file.'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str,
                            help='The path to the CSV file to import')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']
        max_rows = 1000  # Maximum number of rows to import

        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            flights = []
            for i, row in enumerate(reader):
                if i >= max_rows:
                    break  # Stop after importing 1000 rows

                flight_data = {}
                for field in Flight._meta.fields:
                    if field.name.upper() in reader.fieldnames:
                        # Get the value from CSV or set a default value if the string is empty
                        value = row[field.name.upper()].strip() or None
                        if value is not None:
                            if isinstance(field, (models.IntegerField, models.FloatField)) and value == '':
                                # or any other default value that makes sense for your data
                                flight_data[field.name] = 0
                            else:
                                try:
                                    flight_data[field.name] = field.to_python(
                                        value)
                                except ValueError:
                                    # or any other default value
                                    flight_data[field.name] = 0
                        else:
                            flight_data[field.name] = None

                flights.append(Flight(**flight_data))

            # Use Django's bulk_create to import all flights at once
            with transaction.atomic():
                Flight.objects.bulk_create(flights)

        self.stdout.write(self.style.SUCCESS(
            f'{max_rows} rows of flight data imported successfully.'))
