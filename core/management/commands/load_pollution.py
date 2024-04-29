from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings
import csv
from ...models import Pollution
import pandas as pd
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        file = settings.BASE_DIR / 'data' / 'pollution.csv'

        with open(file, 'r') as pol:
            # print(pol.read())
        #     a = []
        #     reader = csv.DictReader(pol)
        #     for row in reader:
        #         # print(row['unit'])
        #         data = {
        #             'date': row['utc'],
        #             'value': row['value'],
        #             'unit': row['unit']
        #         }
        #         a.append(data)


        # df = pd.DataFrame(a)
       
        # pm25_data = df[df['unit'] == 'µg/m³']

            df = pd.read_csv(file, encoding='UTF-8')
            a = []
            for index, row in df.iterrows():
                data = datetime.strptime(row['utc'], "%Y-%m-%d")
            a.append(
                Pollution (
                    time = df['utc'],
                    value = df['value']

                )
            )

            Pollution.objects.abulk_create(a)


        # print(pm25_data)
            

