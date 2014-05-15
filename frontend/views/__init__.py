from ..utils import json_response
from ..models import Size, Supplier, RoyaltyImg, Medium, PriceLevelGroup


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


def ajax_lookup_royalty_img(request):
    return ajax_lookup(request, RoyaltyImg)


def ajax_lookup_medium(request):
    return ajax_lookup(request, Medium)


def ajax_lookup_price_level_group(request):
    return ajax_lookup(request, PriceLevelGroup)