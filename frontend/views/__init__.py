from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from ..utils import json_response
from ..models import Size, Supplier, Medium, RoyaltyGroup, Company, OrderStatus, Catalog


def ajax_lookup_states(request):
    if request.is_ajax():
        states = {
            'ACT': 'Australian Capital Territory',
            'NSW': 'New South Wales',
            'NT': 'Northern Territory',
            'QLD': 'Queensland',
            'SA': 'South Australia',
            'TAS': 'Tasmania',
            'VIC': 'Victoria',
            'WA': 'Western Australia',
            'AJAX': 'I\'ve been loaded via ajax',
            'OS': 'Overseas/Other'
        }
    else:
        states = {
            'NOTAJAX': 'Not an AJAX Request'
        }

    return json_response(states)


def ajax_lookup_order_status(request):
    if request.is_ajax():
        ret = {}
        for o in OrderStatus.ORDER_STATUS_CHOICES:
            ret.update({o[0]: o[1]})
    else:
        ret = {
            'NOTAJAX': 'Not an AJAX Request'
        }

    return json_response(ret)


def ajax_lookup(request, model):
    if request.is_ajax():
        ret = {}
        for s in model.objects.all():
            ret.update({s.pk: str(s)})
    else:
        ret = {
            'NOTAJAX': 'Not an AJAX Request'
        }
    return json_response(ret)


def ajax_lookup_size(request):
    return ajax_lookup(request, Size)


def ajax_lookup_supplier(request):
    return ajax_lookup(request, Supplier)


def ajax_lookup_medium(request):
    return ajax_lookup(request, Medium)


def ajax_lookup_royalty_group(request):
    return ajax_lookup(request, RoyaltyGroup)


def ajax_lookup_company(request):
    return ajax_lookup(request, Company)


def ajax_lookup_catalog(request):
    ret = []
    if request.is_ajax():
        for s in Catalog.objects.all():
            ret.append([0, str(s)])
            for ss in s.issues.all():
                ret.append([ss.pk, str(ss.issue)])

    return json_response(ret)


class IndexView(TemplateView):
    template_name = 'base.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(IndexView, self).dispatch(request, *args, **kwargs)


index_entry = IndexView.as_view()