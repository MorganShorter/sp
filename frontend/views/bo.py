from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from ..models import BackOrder
from ..mixins import TacoMixin
from ..utils import json_response


class BackOrderList(TacoMixin, ListView):
    model = BackOrder
    template_name = 'taconite/bo/list.xml'

obj_list = BackOrderList.as_view()


@login_required
def obj_update(request):
    obj_id = 1
    updated = True

    return json_response({
        'obj_id': obj_id,
        'updated': updated
    })

