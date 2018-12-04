from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render_to_response



counter_show = Counter()
counter_click = Counter()


def index(request):
    if request.GET.get('from-landing') == 'origin':
        counter_click['origin'] =+ 1

    if request.GET.get('from-landing') == 'test':
        counter_click['test'] =+ 1
        
    return render_to_response('index.html')


def landing(request):
    landing = 'landing.html'

    if request.GET.get('ab-test-arg') == 'origin':
        counter_show['origin'] =+ 1

    if request.GET.get('ab-test-arg') == 'test':
        landing = 'landing_alternate.html'
        counter_show['test'] =+ 1

    return render_to_response(landing)


def stats(request):
    result_origin = counter_click['origin'] / counter_show['origin'] if counter_show['origin'] else 0
    result_test = counter_click['test'] / counter_show['test'] if counter_show['test'] else 0

    return render_to_response('stats.html', context={
        'test_conversion': result_test,
        'original_conversion': result_origin,
    })
