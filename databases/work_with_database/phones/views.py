from django.shortcuts import render
from .import_phones import handle
from .models import Phone


def show_catalog(request):
    handle()
    return render(
        request,
        'catalog.html',
        context ={'phones' : Phone.phones}
    )


def show_product(request, slug):
    return render(
        request,
        'product.html',
    )
