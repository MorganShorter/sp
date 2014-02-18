
class TacoMixin(object):
    content_type = 'application/xml'

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