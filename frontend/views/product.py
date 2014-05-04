from django.views.generic import ListView
from ..models import Product
from ..mixins import TacoMixin
from .. import formfields
from . import __taco_render, __preprocess_get_request


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