from django import template
from django.template import defaultfilters

register = template.Library()

@register.assignment_tag
def filterproxy(value, filters):
    ret = value

    if filters:
        for filter_to_use in filters.split('|'):
            filter_args = filter_to_use.split(':')
            func = filter_args.pop(0)

            if hasattr(defaultfilters, func):
                ret = getattr(defaultfilters, func)(ret, *filter_args)

    return ret

@register.filter
def total_sum(arr):
    sum = 0
    for o in arr:
        sum += o.sub_total

    return sum