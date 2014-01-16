import json
#import yaml
from django.http import Http404, HttpResponse
from django.shortcuts import render, render_to_response
from frontend.models import Customer, Order, Invoice
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.core.context_processors import csrf
from django.template import loader, Context

def customer_get(request, pk):
    pk, params = __preprocess_request(request, pk)
    errors = []
    customer = {}

    if pk:
        try:
            customer = Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            errors.append('No customer found with id %s' % (pk))
    else:
        errors.append('No primary key given')

    taco_controlplate = loader.get_template('taconite/customer.xml')
    c_royal = Context({'errors': errors, 'customer': customer})
    c_royal.update(csrf(request))

    return HttpResponse(taco_controlplate.render(c_royal), content_type='application/xml')

#@csrf_exempt
def customer_save(request, pk):
    print request.body
    print request.body.__class__.__name__
    for customer in serializers.deserialize('json', request.body):
        print customer
        print customer.object
        if customer.object.__class__ == Customer:
            if not customer.object.id:
                new_customer = True
                customer.object.slug = None;
            else:
                new_customer = False

            customer.save()

            if new_customer:
                msg = 'Customer created (ID:%d)' % (customer.object.id)
            else:
                msg = 'Customer saved'
        else:
            msg = 'Did not receive expected object Customer. You sent me a %s' % (customer.object.__class__.__name__)

    return HttpResponse(json.dumps(msg), content_type='application/json')

def customer_delete(request, pk):
    pk, params = __preprocess_request(request, pk)

    return HttpResponse('<p>Not Implemented</p>', content_type='text/html')

def __preprocess_request(request, pk):
    if request.method == 'POST':
        params = request.POST
    elif request.method == 'GET':
        params = request.GET
    else:
        params = {}

    if not pk and params.has_key('id'):
        pk = params['id']

    return pk, params


@csrf_exempt
def ajax_save_customer(request, pk):
    data = {'msg': 'No customer was sent!'}
    print request
    if request.POST.has_key('customer'):
        print 'POST has customer'
        for obj in serializers.deserialize('json', request.POST['customer']):
            print '--'
            print 'type(obj):', type(obj)
            print 'obj:', obj
            print 'obj.object:', obj.object
            obj.save()
            data = {'msg': 'Customer saved!'}

    return HttpResponse(json.dumps(data), content_type='application/json')

def serialize_models(data_dict):
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

            data = jsonify_models({'order': order, 'customer': order.customer, 'contacts': order.customer.contacts.all(), 'order_products': order.orderproduct_set.all(), 'products': order.products.all(), 'invoice': invoice, 'company': invoice.company})
        except Order.DoesNotExist:
            pass

    return HttpResponse(data, content_type='application/json')

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

    return HttpResponse(json.dumps(states), content_type='application/json')




# Old Style lookup functions
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
