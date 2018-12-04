from .settings import BUS_STATION_CSV
import csv
from django.shortcuts import render_to_response, redirect, render
from django.urls import reverse
from django.core.paginator import Paginator



def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    all_stations = []
    page_number = request.GET.get('page', 1)

    with open(BUS_STATION_CSV, encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for info in reader:
            bus_stations = {'Name' : info['Name'],
                            'Street': info['Street'],
                            'District': info['District']}
            all_stations.append(bus_stations)

    paginator = Paginator(all_stations, 10)
    page = paginator.get_page(page_number)

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    return render(request, 'index.html', context = {'bus_stations': page,
                                                    'current_page': page_number,
                                                    'prev_page_url': prev_url,
                                                    'next_page_url': next_url,})
