from django.db.models import ProtectedError
from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required

from ..models import Catalog
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class CatalogList(TacoMixin, ListView):
    model = Catalog
    template_name = 'taconite/catalog/list.xml'

obj_list = CatalogList.as_view()


@login_required
def obj_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, Catalog)
    fields = formfields.CatalogForm(obj)
    return __taco_render(request, 'taconite/catalog/item.xml', {
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
            if obj.object.__class__ == Catalog:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    msg = 'Catalog created (ID:%d)' % obj.object.id
                else:
                    obj.save()
                    saved = True
                    msg = 'Catalog saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object Catalog. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'
        print 'Error - %s' % e

    return json_response({
        'saved': saved,
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False
    })


@login_required
def obj_delete(request, pk):
    try:
        pl = Catalog.objects.get(pk=pk)
    except Catalog.DoesNotExist:
        return json_response({
            'status': 'error',
            'msg': 'Wrong ID'
        })

    try:
        pl.delete()
    except ProtectedError:
        return json_response({
            'status': 'error',
            'msg': 'You can`t delete this record because it is used!'
        })

    return json_response({
        'status': 'ok',
        'msg': 'Catalog has been deleted!'
    })