from django.conf import settings
from .models import Phone
import csv


def handle():
    with open(settings.PHONE_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        reader = list(reader)
        for phone_stat in reader:
            for value in phone_stat.values():
                value = value.split(';')
                ph = Phone.objects.get_or_create(id=value[0], name=value[1], image=value[2], price=value[3], release_date=value[4], lte_exists=value[5])
                print(ph)
                print(value)
                print('1111111 ', value)
                # print(phone_stat[value])
            # print(dir(phone_stat))

            # print(dir(phone_stat))
