from django.db.models import ProtectedError
from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required

from ..models import RoyaltyGroup
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class RoyaltyList(TacoMixin, ListView):
    model = RoyaltyGroup
    template_name = 'taconite/royalty/list.xml'

obj_list = RoyaltyList.as_view()


@login_required
def obj_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, RoyaltyGroup)
    fields = formfields.RoyaltyGroupForm(obj)
    return __taco_render(request, 'taconite/royalty/item.xml', {
        'error': error,
        'fields': fields,
        'obj': obj,
    })


@login_required
def obj_save(request):
    msg = ''
    new_obj = False
    obj_id = None
    saved = False
    try:
        for obj in serializers.deserialize('json', request.body):
            if obj.object.__class__ == RoyaltyGroup:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    msg = 'RoyaltyGroup created (ID:%d)' % obj.object.id
                else:
                    obj.save()
                    saved = True
                    msg = 'RoyaltyGroup saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object RoyaltyGroup. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'

    return json_response({
        'saved': saved,
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False
    })


@login_required
def obj_delete(request, pk):
    try:
        pl = RoyaltyGroup.objects.get(pk=pk)
    except RoyaltyGroup.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })

    try:
        pl.delete()
    except ProtectedError:
        return json_response({
            'status': 'error',
            'msg': 'You cant delete this record because it is used!'
        })

    return json_response({
        'status': 'ok',
        'msg': 'Price Level group has been deleted!'
    })