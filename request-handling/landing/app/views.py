from collections import Counter
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request, ):
    count = request.GET.get('from-landing')
    if count == 'origin':
        counter_click['origin'] =+ 1
        return HttpResponse(<h1> counter_click['origin'] </h1>)

    if count == 'test':
        counter_click['test'] =+ 1
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    return render_to_response('index.html')


def landing(request):
    landing = 'landing.html'
    alternate = 'landing_alternate.html'
    review = landing

    if request.GET.get('ab-test-arg') == 'origin':
        review = landing
        counter_show['origin'] =+ 1

    if request.GET.get('ab-test-arg') == 'test':
        review = alternate
        counter_show['test'] =+ 1

    return render_to_response(review)
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    # return render_to_response('landing.html')


def stats(request):
    print(counter_click['origin'])
    print(counter_show['origin'])
    print(counter_click['test'])
    print(counter_show['test'])
    try:
        result_origin = counter_click['origin'] / counter_show['origin']
    except ZeroDivisionError:
        result_origin = 0.0

    try:
        result_test = counter_click['test'] / counter_show['test']
    except ZeroDivisionError:
        result_test = 0.0
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': result_test,
        'original_conversion': result_origin,
    })
