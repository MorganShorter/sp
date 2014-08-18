from django.views.generic import ListView
from ..mixins import MyobMixin


class ServiceSaleList(MyobMixin, ListView):
    pass

service_sale_list = ServiceSaleList.as_view()


class CustomerList(MyobMixin, ListView):
    pass

customer_list = CustomerList.as_view()