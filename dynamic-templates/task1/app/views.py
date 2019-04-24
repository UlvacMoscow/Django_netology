import csv
from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
import collections




class InflationView(TemplateView):
    template_name = 'inflation.html'


    def get(self, request, *args, **kwargs):
        with open (settings.INFLATION_RUSSIA, encoding='utf8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter = ';')
            reader = list(reader)
            keys_table = reader.pop(0)
            keys_table['Всего'] = keys_table.pop('Суммарная')
            context = {'reader': reader, 'keys_table': keys_table }
            return render(request, self.template_name,
                        context)
