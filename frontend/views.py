import json
import frontend.formfields
from django.http import HttpResponse
from frontend.models import Customer, Order, Invoice
from django.core import serializers
from django.template import loader, RequestContext


def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = Invoice()

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = frontend.formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order.xml', {'error':error, 'fields': fields, 'order': order})


def customer_get(request, pk):
    pk, params, customer, error = __preprocess_get_request(request, pk, Customer)
    fields = frontend.formfields.CustomerForm(customer)
    return __taco_render(request, 'taconite/customer.xml', {'error': error, 'fields': fields, 'customer': customer})


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


def __preprocess_get_request(request, pk, model):
    error = None
    obj = None

    if request.method == 'POST':
        params = request.POST
    elif request.method == 'GET':
        params = request.GET
    else:
        params = {}

    if not pk and params.has_key('id'):
        pk = params['id']

    if pk:
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            error = 'No %s found with id %s' % (model.__class__.__name__, pk)
    else:
        error = 'No primary key given to find %s' % model.__class__.__name__

    return pk, params, obj, error


def __taco_render(request, template, context):
    taco_controlplate = loader.get_template(template)
    c_royal = RequestContext(request, context)
    return HttpResponse(taco_controlplate.render(c_royal), content_type='application/xml')


def ajax_lookup_states(request):
    if request.is_ajax():
        states = {
            'ACT': 'Australian Capital Territory',
            'NSW': 'New South Wales',
            'NT': 'Northern Territory',
            'QLD': 'Queensland',
            'SA': 'South Australia',
            'TAS': 'Tasmania',
            'VIC': 'Victoria',
            'WA': 'Western Australia',
            'AJAX': 'I\'ve been loaded via ajax',
            'OS': 'Overseas/Other'
        }
    else:
        states = {
            'NOTAJAX': 'Not an AJAX Request'
        }

    return HttpResponse(json.dumps(states), content_type='application/json')

