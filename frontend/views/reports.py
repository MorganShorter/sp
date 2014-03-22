from datetime import datetime
from django.views.generic import ListView
from django.db.models import Count, Min, Sum, Avg
from ..models import Order
from ..mixins import ReportsMixin


# Sales Order Listing
class Report1(ReportsMixin, ListView):
    model = Order
    template_name = 'taconite/reports/report_1.xml'
    pdf_template = 'reports/pdf/report_1.html'
    csv_template = 'reports/csv/report_1.txt'

    pdf_name = 'report1.pdf'
    csv_name = 'report1.csv'

    def get_queryset(self):
        dfrom = self.request.GET.get('from', None)
        dto = self.request.GET.get('to', None)
        qs = super(Report1, self).get_queryset().filter(statuses__status='SD')

        if dfrom:
            dfrom = datetime.strptime(dfrom, '%Y-%m-%d')
            qs = qs.filter(order_date__gte=dfrom)

        if dto:
            dto = datetime.strptime(dto, '%Y-%m-%d')
            qs = qs.filter(order_date__lte=dto)
        return qs.order_by('-order_date')

report_1 = Report1.as_view()


# Top Sellers
class Report2(ReportsMixin, ListView):
    model = Order
    template_name = 'taconite/reports/report_2.xml'
    pdf_template = 'reports/pdf/report_2.html'
    csv_template = 'reports/csv/report_2.txt'

    pdf_name = 'report2.pdf'
    csv_name = 'report2.csv'

    def get_queryset(self):
        dfrom = self.request.GET.get('from', None)
        dto = self.request.GET.get('to', None)
        qs = super(Report2, self).get_queryset().filter(statuses__status='SD')

        if dfrom:
            dfrom = datetime.strptime(dfrom, '%Y-%m-%d')
            qs = qs.filter(order_date__gte=dfrom)

        if dto:
            dto = datetime.strptime(dto, '%Y-%m-%d')
            qs = qs.filter(order_date__lte=dto)

        return qs.values('customer__pk', 'customer__name', 'customer__customer_type').annotate(total=Sum('total_cost')).filter(total__gt=0).order_by('-total')[:100]

report_2 = Report2.as_view()