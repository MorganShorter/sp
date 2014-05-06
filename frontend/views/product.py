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
    new_obj = False
    for obj in serializers.deserialize('json', request.body):
        if obj.object.__class__ == Product:
            if not obj.object.id:
                print 'new obj'
                new_obj = True
                #obj.object.set_slug()

            obj.save()

            if new_obj:
                msg = 'Product created (ID:%d)' % obj.object.id
            else:
                msg = 'Product saved'
        else:
            msg = 'Did not receive expected object Product. You sent me a %s' % obj.object.__class__.__name__

    return json_response({
        'msg': msg,
        'obj_id': obj.object.id,
        'created': True if new_obj else False
    })