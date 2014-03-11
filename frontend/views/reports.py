from datetime import datetime
from django.views.generic import ListView
from ..models import Order


# Sales Order Listing
class Report1(ListView):
    model = Order
    template_name = 'taconite/report_1.xml'

    def get_queryset(self):
        dfrom = self.request.GET.get('from', None)
        dto = self.request.GET.get('to', None)
        qs = super(Report1, self).get_queryset()

        if dfrom:
            dfrom = datetime.strptime(dfrom, '%Y-%m-%d')
            qs = qs.filter(order_date__gte=dfrom)

        if dto:
            dto = datetime.strptime(dto, '%Y-%m-%d')
            qs = qs.filter(order_date__lte=dto)
        return qs

report_1 = Report1.as_view()