import cStringIO as StringIO
from cgi import escape
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


try:
    import ho.pisa as pisa
except ImportError:
    print 'pisa import error'


class MyobMixin(object):
    content_type = 'text/csv'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MyobMixin, self).dispatch(request, *args, **kwargs)


class TacoMixin(object):
    content_type = 'application/xml'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        self.context = context = dict(kwargs)

        return super(TacoMixin, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        super_context = super(TacoMixin, self).get_context_data(**kwargs)
        context = self.context

        if super_context:
            context.update(super_context)
        return context


class ReportsMixin(object):
    pdf_template = ''
    csv_template = ''
    pdf_name = 'report.pdf'
    csv_name = 'report.csv'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(ReportsMixin, self).dispatch(request, *args, **kwargs)

    def get_csv_name(self):
        return self.csv_name

    def get_pdf_name(self):
        return self.pdf_name

    def render_to_response(self, context, **kwargs):
        import_format = self.request.GET.get('format', None)
        if import_format:
            if import_format == 'csv':
                return self.render_to_csv(context, **kwargs)
            if import_format == 'pdf':
                return self.render_to_pdf(context, **kwargs)
        return super(ReportsMixin, self).render_to_response(context, **kwargs)

    def render_to_pdf(self, context, **kwargs):
        self.template_name = self.pdf_template
        ret = super(ReportsMixin, self).render_to_response(context, **kwargs)
        html = ret.rendered_content
        result = StringIO.StringIO()
        pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            resp = HttpResponse(result.getvalue(), mimetype='application/pdf')
            resp['Content-Disposition'] = 'attachment; filename="%s"' % self.get_pdf_name()
            return resp
        return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

    def render_to_csv(self, context, **kwargs):
        self.template_name = self.csv_template
        ret = super(ReportsMixin, self).render_to_response(context, **kwargs)
        resp = HttpResponse(ret.rendered_content, mimetype='text/csv')
        resp['Content-Disposition'] = 'attachment; filename="%s"' % self.get_csv_name()
        return resp