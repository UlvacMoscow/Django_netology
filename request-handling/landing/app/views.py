from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render_to_response



counter_show = Counter()
counter_click = Counter()


def index(request):
    from_landing = request.GET.get('from-landing')
    counter_click[from_landing] =+ 1

    return render_to_response('index.html')


def landing(request):
    landing = 'landing.html'
    ab_test_arg = request.GET.get('ab-test-arg')

    if ab_test_arg == 'test':
        landing = 'landing_alternate.html'
        
    counter_show[ab_test_arg] =+ 1
    return render_to_response(landing)


def stats(request):
    result_origin = counter_click['origin'] / counter_show['origin'] if counter_show['origin'] else 0
    result_test = counter_click['test'] / counter_show['test'] if counter_show['test'] else 0

    return render_to_response('stats.html', context={
        'test_conversion': result_test,
        'original_conversion': result_origin,
    })
