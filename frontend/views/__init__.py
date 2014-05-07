from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields
from ..models import Order, Invoice, Size, Supplier, RoyaltyImg, Medium


def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = Invoice()

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order.xml', {'error': error, 'fields': fields, 'order': order})


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

    return json_response(states)


def ajax_lookup(request, model):
    if request.is_ajax():
        ret = {}
        for s in model.objects.all():
            ret.update({s.pk: str(s)})
    else:
        ret = {
            'NOTAJAX': 'Not an AJAX Request'
        }
    return json_response(ret)


def ajax_lookup_size(request):
    return ajax_lookup(request, Size)


def ajax_lookup_supplier(request):
    return ajax_lookup(request, Supplier)


def ajax_lookup_royalty_img(request):
    return ajax_lookup(request, RoyaltyImg)


def ajax_lookup_medium(request):
    return ajax_lookup(request, Medium)