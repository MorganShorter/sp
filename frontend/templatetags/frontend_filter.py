from django import template

register = template.Library()


@register.filter
def total_sum(arr):
    sum = 0
    for o in arr:
        sum += o.total_cost
    return sum