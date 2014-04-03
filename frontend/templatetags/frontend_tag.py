from django import template
from ..models import Customer

register = template.Library()

@register.assignment_tag
def get_customer_contacts(customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        return ''

    return customer.contacts.all()