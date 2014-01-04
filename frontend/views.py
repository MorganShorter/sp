from django.http import Http404
from django.shortcuts import render
from frontend.models import Customer

# Create your views here.
def customer_detail(request, customer_id="1"):
#    raise Http404
    try:
        customer = Customer.objects.get(pk=customer_id)
        customer_contacts = customer.contacts.all()
    except Customer.DoesNotExist:
        raise Http404

#    return render_to_response('base.html', {'customer': customer})

    return render(request, 'base.html', {'customer': customer, 'customer_contacts': customer_contacts})
