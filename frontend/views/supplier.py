from django.views.generic import ListView
from django.core import serializers
from django.contrib.auth.decorators import login_required

from ..models import Supplier
from ..mixins import TacoMixin
from ..utils import __preprocess_get_request, __taco_render, json_response
from .. import formfields


class SupplierList(TacoMixin, ListView):
    model = Supplier
    template_name = 'taconite/Supplier/list.xml'

obj_list = SupplierList.as_view()


@login_required
def obj_get(request, pk):
    pk, params, obj, error = __preprocess_get_request(request, pk, Supplier)
    fields = formfields.SupplierForm(obj)
    return __taco_render(request, 'taconite/Supplier/item.xml', {
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
            if obj.object.__class__ == Supplier:
                if not obj.object.id:
                    new_obj = True
                    obj.save()
                    saved = True
                    msg = 'Supplier created (ID:%d)' % obj.object.id
                else:
                    obj.save()
                    saved = True
                    msg = 'Supplier saved'

                obj_id = obj.object.id
            else:
                msg = 'Did not receive expected object Supplier. You sent me a %s' % obj.object.__class__.__name__

    except Exception, e:
        msg = 'Wrong values'

    return json_response({
        'saved': saved,
        'msg': msg,
        'obj_id': obj_id,
        'created': True if new_obj else False
    })