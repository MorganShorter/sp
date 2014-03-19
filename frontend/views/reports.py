from datetime import datetime
from django.http import HttpResponse
from django.views.generic import ListView
from ..models import Order


# Sales Order Listing
class Report1(ListView):
    model = Order
    template_name = 'taconite/report_1.xml'

    def render_to_response(self, context, **kwargs):
        import_format = self.request.GET.get('format', None)
        if import_format:
            if import_format == 'csv':
                self.template_name = 'reports/csv/report_1.txt'
                ret = super(Report1, self).render_to_response(context, **kwargs)
                resp = HttpResponse(ret.rendered_content, mimetype='text/xml')
                resp['Content-Disposition'] = 'attachment; filename="report1.csv"'
                return resp

        return super(Report1, self).render_to_response(context, **kwargs)

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