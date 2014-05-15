from django.views.generic import ListView
from ..utils import __preprocess_get_request, __taco_render
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
    invoice = Invoice()

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order/item.xml', {
        'error': error,
        'fields': fields,
        'order': order}
    )