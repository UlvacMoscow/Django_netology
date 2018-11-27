import csv
from .settings import INFLATION_RUSSIA
from django.shortcuts import render
from django.views.generic import TemplateView
import collections




class InflationView(TemplateView):
    template_name = 'inflation.html'


    def get(self, request, *args, **kwargs):
        all_stats = []

        with open (INFLATION_RUSSIA, encoding='utf8') as csvfile:
            reader = csv.reader(csvfile, delimiter = ';')
            reader = list(reader)
            temp = reader.pop(0)
            for stat_row in reader:
                full_row = {}
                for num in range(len(temp)):
                    full_row[temp[num]] = stat_row[num]
                all_stats.append(full_row)

        for st in all_stats:
            print(st)

        # чтение csv-файла и заполнение контекста
        context = {}
        return render(request, self.template_name,
                      context)
