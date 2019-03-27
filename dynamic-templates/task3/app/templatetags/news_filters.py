from django import template
from datetime import datetime as dt

register = template.Library()

@register.filter
def format_date(value):
    now = dt.now()
    print('111111111 ', now)
    then = dt.fromtimestamp(value)
    print('1111111112 ', then)
    delta = now - then
    print('1111111113 ', delta)
    hours = delta.seconds // 3600
    print('1111111114 ', dir(hours))

    if delta.seconds // 60 < 10:
        return 'Только что'
    elif hours < 24:
        return '{} часов назад'.format(hours)
    return dt.fromtimestamp(delta).strftime("%Y-%m-%d")



@register.filter
def format_score(value=0):
    if value < -5:
        return 'все плохо'
    elif value > 5:
        return 'хорошо'
    return 'нейтрально'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value < 50:
        return value
    return '50+'


@register.filter
def format_selftext(text, count):
    temp = text.split()
    if len(temp) > 2 * count:
        return '{0} ... {1}'.format(' '.join(temp[:count]), ' '.join(temp[-count:]))
    return text
