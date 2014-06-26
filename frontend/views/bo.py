from datetime import datetime
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from ..models import BackOrder
from ..mixins import TacoMixin
from ..utils import json_response


class BackOrderList(TacoMixin, ListView):
    model = BackOrder
    template_name = 'taconite/bo/list.xml'

    def get_queryset(self):
        dfrom = self.request.GET.get('from', None)
        dto = self.request.GET.get('to', None)
        complete = bool(self.request.GET.get('complete', False))

        qs = super(BackOrderList, self).get_queryset().filter(complete=complete)

        if dfrom:
            dfrom = datetime.strptime(dfrom, '%Y-%m-%d')
            qs = qs.filter(timestamp__gte=dfrom)

        if dto:
            dto = datetime.strptime(dto, '%Y-%m-%d')
            qs = qs.filter(timestamp__lte=dto)

        return qs.order_by('-timestamp')

obj_list = BackOrderList.as_view()


@login_required
def obj_update(request):
    bo_id = request.GET.get('bo_id', None)
    obj = get_object_or_404(BackOrder, pk=bo_id)

    obj.complete = not obj.complete
    obj.save()

    return json_response({
        'obj_id': obj.pk,
        'updated': True
    })

