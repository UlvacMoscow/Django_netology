from django import template
from datetime import datetime as dt


register = template.Library()


@register.filter
def format_date(value):
    now = dt.now()
    then = dt.fromtimestamp(value)
    delta = now - then
    hours = delta.seconds // 3600

    if delta.seconds // 60 < 10:
        return 'Только что'
    elif hours < 24:
        return '{} часов назад'.format(hours)
    else:
        return dt.fromtimestamp(delta).strftime("%Y-%m-%d")
    return then


@register.filter
def format_score(value=0):
    if value < -5:
        return 'все плохо'
    elif value > 5:
        return 'хорошо'
    else:
        return 'нейтрально'


@register.filter
def format_num_comments(value):
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value < 50:
        return value
    else:
        return '50+'
    return value


@register.filter
def format_selftext(text, count):
    temp = text.split()
    if len(temp) - 1 > 2 * count:
        return '{0} ... {1}'.format(' '.join(temp[:count]), ' '.join(temp[-count:]))
    return text
