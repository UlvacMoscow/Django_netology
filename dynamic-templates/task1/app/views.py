import csv
from .settings import INFLATION_RUSSIA
from django.shortcuts import render
from django.views.generic import TemplateView




class InflationView(TemplateView):
    template_name = 'inflation.html'

    def get(self, request, *args, **kwargs):
        with open (INFLATION_RUSSIA, encoding=None) as csvfile:
            reader = csv.DictReader(csvfile)
            
        # чтение csv-файла и заполнение контекста
        context = {}
        return render(request, self.template_name,
                      context)
