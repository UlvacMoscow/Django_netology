from django.shortcuts import render
from .models import Asus, Nokia, Xiomi


def show_catalog(request):
    asus = Asus.objects.all()
    nokia = Nokia.objects.all()
    xiaomi = Xiomi.objects.all()
    return render(
        request,
        'catalog.html',
        context={
            'asus': asus,
            'nokia': nokia,
            'xiaomi': xiaomi
        }
    )


def show_phones(request):
    phones = Nokia.objects.all()

    return render(
        request,
        'phones.html',
        context={
            'phones':phones
        }
    )
