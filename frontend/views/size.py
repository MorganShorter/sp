from django.db.models import ProtectedError
from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required

from ..models import Size
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class SizeList(TacoMixin, ListView):
    model = Size
    template_name = 'taconite/size/list.xml'

obj_list = SizeList.as_view()


@login_required
def obj_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, Size)
    fields = formfields.SizeForm(obj)
    return __taco_render(request, 'taconite/size/item.xml', {
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
            if obj.object.__class__ == Size:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    msg = 'Size created (ID:%d)' % obj.object.id
                else:
                    obj.save()
                    saved = True
                    msg = 'Size saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object Size. You sent me a %s' % obj.object.__class__.__name__

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
        pl = Size.objects.get(pk=pk)
    except Size.DoesNotExist:
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
        'msg': 'Size object has been deleted!'
    })