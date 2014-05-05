import json
from django.http import HttpResponse
from django.template import loader, RequestContext

from .. import formfields
from ..models import Order, Invoice, Size, Supplier, RoyaltyImg


def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = Invoice()

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order.xml', {'error':error, 'fields': fields, 'order': order})


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


def ajax_lookup(request, model):
    if request.is_ajax():
        ret = {}
        for s in model.objects.all():
            ret.update({s.pk: str(s)})
    else:
        ret = {
            'NOTAJAX': 'Not an AJAX Request'
        }
    return HttpResponse(json.dumps(ret), content_type='application/json')


def ajax_lookup_size(request):
    return ajax_lookup(request, Size)


def ajax_lookup_supplier(request):
    return ajax_lookup(request, Supplier)


def ajax_lookup_royalty_img(request):
    return ajax_lookup(request, RoyaltyImg)