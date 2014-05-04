from django.views.generic import ListView
from ..models import Product
from ..mixins import TacoMixin


class ProductList(TacoMixin, ListView):
    model = Product
    template_name = 'taconite/customer_list.xml'

    def get_queryset(self):
        qs = super(ProductList, self).get_queryset()
        fltr = {}
        if self.request.GET.get('customer_id', None):
            fltr['pk'] = self.request.GET['customer_id']

        if self.request.GET.get('find_customer_name', None):
            fltr['name__icontains'] = self.request.GET['find_customer_name']

        if self.request.GET.get('find_customer_phone', None):
            fltr['telephone__icontains'] = self.request.GET['find_customer_phone']

        if self.request.GET.get('find_customer_email', None):
            fltr['email__icontains'] = self.request.GET['find_customer_email']

        if not fltr:
            return qs.none()

        return qs.filter(**fltr)


product_list = ProductList.as_view()