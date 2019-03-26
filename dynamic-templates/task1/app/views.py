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
            print('111111 ', reader)
            for row in reader:
                print(row)
            context = {'reader': reader}
        return render(request, self.template_name,
                      context)
