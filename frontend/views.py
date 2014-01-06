import json
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response
from frontend.models import Customer, Order, Invoice
from django.core import serializers

# Create your views here.
def customer_detail(request, customer_id="1"):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404

    return render(request, 'base.html', {'customer': customer})
    #return render_to_response('base.html', {'customer': customer})

def ajax_lookup_customer(request):
    data = json.dumps(None)
    if request.GET.has_key('customer_id'):
        try:
            customer = Customer.objects.get(pk=request.GET['customer_id'])
            data = jsonify_models({'customer': customer, 'contacts': customer.contacts.all()})
        except Customer.DoesNotExist:
            pass

    return HttpResponse(data, mimetype='application/json')

def jsonify_models(data_dict):
    json_string = None
    for model_key, model_data in data_dict.iteritems():
        if model_data.__class__.__name__ != 'QuerySet':
            json_model_data = serializers.serialize('json', [model_data])[1:-1]
        else:
            json_model_data = serializers.serialize('json', model_data)

        if not json_string:
            json_string = '{"' + model_key + '": ' + json_model_data
        else:
            json_string += ', "' + model_key + '": ' + json_model_data

    if json_string:
        json_string += '}'
    else:
        json_string = json.dumps(None)

    return json_string
            
def ajax_lookup_order(request):
    data = json.dumps(None)
    if request.GET.has_key('order_id'):
        order_id = request.GET['order_id']
        try:
            order = Order.objects.get(pk=order_id)
            try:
                invoice = Invoice.objects.get(order_id=order_id)
            except Invoice.DoesNotExist:
                invoice = None

            data = jsonify_models({'order': order, 'customer': order.customer, 'contacts': order.customer.contacts.all(), 'order_products': order.orderproduct_set.all(), 'products': order.products.all(), 'invoice': invoice})
        except Order.DoesNotExist:
            pass

    return HttpResponse(data, mimetype='application/json')

def ajax_lookup_states(request):
    if request.is_ajax():
        states = { 'ACT': 'Australian Capital Territory',
                   'NSW': 'New South Wales',
                   'NT': 'Northern Territory',
                   'QLD': 'Queensland',
                   'SA': 'South Australia',
                   'TAS': 'Tasmania',
                   'VIC': 'Victoria',
                   'WA': 'Western Australia',
                   'AJAX': 'I\'ve been loaded via ajax',
                   'OS': 'Overseas/Other' }
    else:
        states = { 'NOTAJAX': 'Not an AJAX Request' }

    return HttpResponse(json.dumps(states), mimetype='application/json')

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
