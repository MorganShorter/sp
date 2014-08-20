from django.views.generic import ListView
from ..mixins import MyobMixin
from ..models import Customer, Order


class ServiceSaleList(MyobMixin, ListView):
    model = Order
    template_name = 'myob/sale.txt'

service_sale_list = ServiceSaleList.as_view()


class CustomerList(MyobMixin, ListView):
    model = Customer
    template_name = 'myob/customer.txt'

customer_list = CustomerList.as_view()