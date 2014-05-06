from django.views.generic import ListView
from django.core import serializers

from ..models import Product
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class ProductList(TacoMixin, ListView):
    model = Product
    template_name = 'taconite/product/list.xml'

    def get_queryset(self):
        qs = super(ProductList, self).get_queryset()
        fltr = {}
        if self.request.GET.get('product_code', None):
            fltr['code'] = self.request.GET['product_code']

        if self.request.GET.get('find_product_name', None):
            fltr['name__icontains'] = self.request.GET['find_product_name']

        if not fltr:
            return qs.none()

        return qs.filter(**fltr)


product_list = ProductList.as_view()


def product_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, Product)
    fields = formfields.ProductForm(obj)
    return __taco_render(request, 'taconite/product/item.xml', {
        'error': error,
        'fields': fields,
        'obj': obj
    })


def product_save(request):
    msg = ''
    new_customer = False
    for customer in serializers.deserialize('json', request.body):
        print customer
        print customer.object
        if customer.object.__class__ == Product:
            if not customer.object.id:
                print 'new customer'
                new_customer = True
                customer.object.set_slug()

            customer.save()

            if new_customer:
                msg = 'Customer created (ID:%d)' % customer.object.id
            else:
                msg = 'Customer saved'
        else:
            msg = 'Did not receive expected object Customer. You sent me a %s' % customer.object.__class__.__name__

    return json_response({
        'msg': msg,
        'customer_id': customer.object.id,
        'creatred': True if new_customer else False
    })