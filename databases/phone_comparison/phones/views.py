from django.shortcuts import render
from .models import Phone, Asus, Nokia, Xiaomi
from django.http import HttpResponse


def show_catalog(request):
    phones = Phone.get_all_phones()
    print(dir(request.GET.get))
    print('111111  ', request.GET.get('phones'))
    return render(
        request,
        'catalog.html',
        context={
            'phones': phones,
        }
    )


def compression_phones(request):
    # phones = Nokia.objects.all()
    phones = Phone.get_all_phones()
    print(dir(phones))
    print(phones.count)
    return render(
        request,
        'compression_phones.html',
        context={
            'phones':phones
        }
    )
