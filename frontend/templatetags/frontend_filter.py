from django import template

register = template.Library()


@register.filter
def total_sum(arr, param='total_cost'):
    sum = 0
    for o in arr:
        sum += getattr(o, param, 0)
    return sum
