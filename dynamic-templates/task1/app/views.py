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
            # dictreader = csv.DictReader(csvfile)
            # print('dictreader ', dictreader)
            # for row in dictreader:
            #     # print(row['Год'])
            #     print(list(row)[0])
            #     print('1 ', row[0])








            reader = csv.reader(csvfile, delimiter = ';')
            reader = list(reader)
            temp = reader.pop(0)
            convert_float = lambda x: '-' if '' else float(x)
            for stat_row in reader:  # reader[1:] со второго элемента
                print('stat_row ',stat_row)
                full_row = {}
                for num in range(len(temp)):
                    if num == 0:
                        full_row[temp[num]] = stat_row[num]
                    elif stat_row[num] == '':
                        full_row[temp[num]] = '-'
                    elif float(stat_row[num]) % 1 == 0:
                        full_row[temp[num]] = int(stat_row[num])
                    else:
                        full_row[temp[num]] = float(stat_row[num])
                all_stats.append(full_row)

        for st in all_stats:
            print(st)

        # чтение csv-файла и заполнение контекста
        context = {'inflation' : all_stats,
                   'columns' : temp,
                   'zero' : 0.31 }
        return render(request, self.template_name,
                      context)
