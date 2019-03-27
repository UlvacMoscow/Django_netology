from django import template

register = template.Library()

@register.filter
def color_filter(stat, key):
    stat = float(stat)
    if key == 'Год':
        return ''
    elif key == "Суммарная":
        return '#bdbdbd grey lighten-1'
    elif stat < 0:
        return '2e7d32 green darken-1'
    elif stat > 1 and stat < 2:
        return 'ffcdd2 red lighten-4'
    elif stat > 2 and stat < 5:
        return 'ef9a9a red lighten-3'
    elif stat > 5:
        return 'b71c1c red darken-4'
    return ''
