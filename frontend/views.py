from django.http import Http404
from django.shortcuts import render, render_to_response
from frontend.models import Customer, Order, Invoice

# Create your views here.
def customer_detail(request, customer_id="1"):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404

    return render(request, 'base.html', {'customer': customer})
    #return render_to_response('base.html', {'customer': customer})

def order_detail(request, order_id="1"):
    try:
        order = Order.objects.get(pk=order_id)

        try:
            invoice = Invoice.objects.get(order_id=order_id)
        except Invoice.DoesNotExist:
            invoice = None

    except Order.DoesNotExist:
        raise Http404

    return render(request, 'base.html', {'order': order, 'order_invoice': invoice})
    #return render_to_response('base.html', {'order': order, 'order_invoice': invoice})
