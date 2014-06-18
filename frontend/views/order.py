import json
from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields
from ..models import Order, Invoice, Company, Customer, OrderStatus, Product, OrderProduct
from ..mixins import TacoMixin


class OrderList(TacoMixin, ListView):
    model = Order
    template_name = 'taconite/order/list.xml'

    def get_queryset(self):
        qs = super(OrderList, self).get_queryset()
        fltr = {}

        if self.request.GET.get('order_customer', None):
            fltr['customer_id'] = self.request.GET['order_customer']

        if self.request.GET.get('order_customer_name', None):
            fltr['customer__name__icontains'] = self.request.GET['order_customer_name']

        if self.request.GET.get('find_order_id', None):
            fltr['pk'] = self.request.GET['find_order_id']

        if self.request.GET.get('find_order_inv_num', None):
            fltr['invoices__number'] = self.request.GET['find_order_inv_num']

        if not fltr:
            if self.request.GET.get('last', None):
                return qs.order_by('-last_read')[:20]
            else:
                return qs.none()

        return qs.filter(**fltr)


order_list = OrderList.as_view()


@login_required
def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = None

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

        if not invoice:
            invoice = Invoice(
                order=order,
                number=order.pk,
                company=Company.objects.first()
            )
            invoice.save()

        if not order.last_status:
            order.statuses.create()

        order.save()  # update last_read date

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order/item.xml', {
        'error': error,
        'fields': fields,
        'order': order,
        'only_products': request.GET.get('only_products', None)
    })


@login_required
def order_create(request, customer_pk):
    order = Order()

    try:
        customer = Customer.objects.get(pk=customer_pk)
        order.customer_id = customer.pk

        order.invoice_company_name = customer.name
        order.invoice_company_reg = customer.registration
        order.invoice_address_line_1 = customer.address_line_1
        order.invoice_address_line_2 = customer.address_line_2
        order.invoice_suburb = customer.suburb
        order.invoice_state = customer.state
        order.invoice_postcode = customer.postcode
        order.invoice_country = customer.country

        order.shipping_attn = customer.delivery_attn
        order.shipping_address_line_1 = customer.delivery_address_line_1
        order.shipping_address_line_2 = customer.delivery_address_line_2
        order.shipping_suburb = customer.delivery_suburb
        order.shipping_state = customer.delivery_state
        order.shipping_postcode = customer.delivery_postcode
        order.shipping_country = customer.delivery_country

        order.save()
    except Exception, e:
        print 'Create order error'
        print e
        return json_response({
            'status': 'error'
        })

    return order_get(request, order.pk)


@login_required
def order_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == Order:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    msg = 'Order created (ID:%d)' % obj.object.id
                else:
                    obj.save()
                    saved = True
                    msg = 'Order saved'

                order_data = json.loads(request.body)[0]
                invoice = order_data.get('invoice', None)
                if obj.object.last_invoice:
                    inv = obj.object.last_invoice
                else:
                    inv = Invoice()
                    inv.order = obj.object

                try:
                    inv.company_id = invoice['company']
                    inv.number = invoice['number']
                    inv.save()
                except Exception, e:
                    print 'Error! Invoice error'

                # products
                products = order_data.get('products', None)
                if products:
                    for pr_obj in products.items():
                        try:
                            order_product = OrderProduct.objects.get(pk=int(pr_obj[0]), order=obj.object)
                        except Exception, e:
                            print 'OrderProduct not found'
                            continue

                        try:
                            order_product.quantity = int(pr_obj[1]['quantity'])
                            order_product.unit_price = float(pr_obj[1]['cost'])
                            order_product.discount_percentage = float(pr_obj[1]['discount'])
                            order_product.with_tax = pr_obj[1]['tax']
                            order_product.save()
                        except Exception, e:
                            print 'OrderProduct save error'
                            print e
                            continue

                    # Recount total
                    obj.object.total_recount(save=True)

                status = json.loads(request.body)[0].get('status', None)
                if status != obj.object.last_status.status:
                    if status in OrderStatus.STATUSES:
                        obj.object.statuses.create(
                            status=status,
                            user=request.user,
                            notes="manually changed by %s" % request.user
                        )

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


@login_required
def order_delete(request, pk):
    try:
        obj = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })
    obj.delete()

    return json_response({
        'status': 'ok',
        'msg': 'Order has deleted!'
    })


@login_required
def order_add_product(request, order_id, product_id):
    try:
        order = Order.objects.get(pk=int(order_id))
        product = Product.objects.get(pk=int(product_id))
    except Exception, e:
        return json_response({
            'status': 'error'
        })

    OrderProduct(
        order=order,
        product=product,
        quantity=1,
        unit_price=product.default_price,
        discount_percentage=0,
    ).save()

    return json_response({
        'status': 'ok'
    })


@login_required
def order_delete_product(request, order_product_id):
    try:
        OrderProduct.objects.get(pk=order_product_id).delete()
    except Exception, e:
        return json_response({
            'status': 'error'
        })

    return json_response({
        'status': 'ok'
    })
