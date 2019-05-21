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
    if request.GET.get('phone_1') and request.GET.get('phone_2'):
        num1 = request.GET.get('phone_1')
        num2 = request.GET.get('phone_2')
        info_phone1 = Phone.objects.get(pk=num1)
        info_phone2 = Phone.objects.get(pk=num2)
        test = {"model_name" : info_phone1.model_name,
                "brand" : info_phone1.brand,
                "processor" : info_phone1.processor,
                "model_name2" : info_phone2.model_name,
                "brand2" : info_phone2.brand,
                "processor2" : info_phone2.processor
                }
        test = json.dumps(test)
        return HttpResponse(test, content_type='application/json')
    return HttpResponse('<h6>Что-то пошло не так</h6>')
