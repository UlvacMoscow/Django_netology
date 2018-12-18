from django.shortcuts import render
from .models import Phone, Nokia, Xiomi


def show_catalog(request):
    phones = Phone.objects.all()
    all_nokia = Nokia.objects.all()
    all_xiomi = Xiomi.objects.all()
    return render(
        request,
        'catalog.html',
        context={
            'phones':phones
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



