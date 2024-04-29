from itertools import islice
import csv
from datetime import date
from django.core.management.base import BaseCommand
from core.models import CarbonEmission  
from django.conf import settings

class Command(BaseCommand):
    help = "reads and loads the data file of co2"

    def handle(self, *args, **kwargs):
        file = settings.BASE_DIR / 'data' / 'co2.csv'

        with open(file, 'r') as co2file:
            reader = csv.DictReader(islice(co2file, 40, None))

            for row in reader:
                dt = date(
                    year=int(row['year']),
                    month=int(row['month']),
                    day = 15
                )
                CarbonEmission.objects.get_or_create(date=dt, average=float(row['average']))
