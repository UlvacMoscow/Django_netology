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
            print('111111 ', dir(reader))
            print('22222  ',reader.fieldnames)
            print('22222  ',reader.__iter__)
            # for r in reader:
            #     print(r)
                # print(r.items())
                # for it in r.items():
                #     print(it[1])


            context = {'reader': reader}
        return render(request, self.template_name,
                      context)
