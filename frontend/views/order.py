from django.views.generic import ListView
from django.core import serializers
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields
from ..models import Order, Invoice
from ..mixins import TacoMixin


class OrderList(TacoMixin, ListView):
    model = Order
    template_name = 'taconite/order/list.xml'

    def get_queryset(self):
        qs = super(OrderList, self).get_queryset()
        fltr = {}

        if self.request.GET.get('order_customer', None):
            fltr['customer_id'] = self.request.GET['order_customer']

        if self.request.GET.get('find_order_id', None):
            fltr['pk'] = self.request.GET['find_order_id']

        if self.request.GET.get('find_order_inv_num', None):
            fltr['invoices__number'] = self.request.GET['find_order_inv_num']

        if not fltr:
            return qs.none()

        return qs.filter(**fltr)


order_list = OrderList.as_view()


def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = None

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order/item.xml', {
        'error': error,
        'fields': fields,
        'order': order
    })


def order_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == Order:
                print 'object decoded'

                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True

                    msg = 'Order created (ID:%d)' % obj.object.id

                else:
                    obj.save()
                    saved = True
                    msg = 'Order saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object Order. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'
        print e

    return json_response({
        'saved': saved,
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False
    })