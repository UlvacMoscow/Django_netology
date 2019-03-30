from django.shortcuts import render
from .models import Asus, Nokia, Xiaomi


def show_catalog(request):
    asus = Asus.objects.all()
    nokia = Nokia.objects.all()
    xiaomi = Xiaomi.objects.all()
    all_models_phone = [*asus, *nokia, *xiaomi]
    return render(
        request,
        'catalog.html',
        context={
            'phones': all_models_phone,
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
