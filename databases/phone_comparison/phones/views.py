from django.shortcuts import render
from .models import Phone, Asus, Nokia, Xiaomi
from django.http import HttpResponse


def show_catalog(request):
    phones = Phone.get_all_phones().order_by('pk')
    # print(dir(request.GET.get))
    # print('111111  ', request.GET.get('phones'))
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
    context = {'phones': phones}
    if request.GET.get('number_phone'):
        # print('попадение', request.GET.get('number_phone'))
        num = request.GET.get('number_phone')

        print('номер телефона', num)
        info_phone = Phone.objects.get(pk=num)
        context['info_phone'] = info_phone
        print('info_phone', info_phone)

    print(context)
    return render(
        request,
        'compression_phones.html',
        context=context
    )
