from django.shortcuts import render, render_to_response
from .models import Phone, Asus, Nokia, Xiaomi
from django.http import HttpResponse, JsonResponse
import json


def show_catalog(request):
    phones = Phone.get_all_phones().order_by('pk')
    return render(
        request,
        'catalog.html',
        context={
            'phones': phones,
        }
    )


def compression_phones(request, *args, **kwargs):
    phones = Phone.get_all_phones()
    context = {'phones': phones}
    if request.GET.get('phone1'):
        num1 = request.GET.get('phone1')
        num2 = request.GET.get('phone2')
        info_phone1 = Phone.objects.get(pk=num1)
        info_phone2 = Phone.objects.get(pk=num2)
        context['info_phone1'] = info_phone1
        context['info_phone2'] = info_phone2

    return render(
        request,
        'compression_phones.html',
        context=context
    )


def ajax(request):

    print(request.GET.get('data'))
    if request.GET.get('phone_1') and request.GET.get('phone_2'):
        num1 = request.GET.get('phone_1')
        num2 = request.GET.get('phone_2')
        print('1111 ', num1, num2)
        info_phone1 = Phone.objects.get(pk=num1)
        info_phone2 = Phone.objects.get(pk=num2)
        print('2222 ', info_phone1.brand)
        # return HttpResponse({'brand' : info_phone1.brand})
        # return JsonResponse({'brand' : info_phone1.brand})
        return render({'brand' : info_phone1.brand})
    print('ajax 11111111111111111111')
    # print(request.GET.get('phone_1'))
    return HttpResponse('<h6>Hello</h6>')
