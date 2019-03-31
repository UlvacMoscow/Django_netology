from django.shortcuts import render
from .import_phones import handle
from .models import Phone


def show_catalog(request):
    phones = Phone.phones()
    if request.GET.get('sort') == 'max_price':
        phones = Phone.max_price
    elif request.GET.get('sort') == 'min_price':
        phones = Phone.min_price
    elif request.GET.get('sort') == 'name':
        phones = Phone.sort_name
    return render(
        request,
        'catalog.html',
        context ={'phones' : phones}
    )


def show_product(request, slug):
    print('111 ', type(slug))
    for cur_phone in Phone.phones():
        if ''.join(cur_phone.name.split()) == slug:
            context = {'phone': cur_phone}
        return render(
            request,
            'product.html',
            context
        )
