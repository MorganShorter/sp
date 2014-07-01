from django.views.generic import ListView
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

from .. import formfields
from ..models import Customer, CustomerContact, Note
from ..mixins import TacoMixin

from ..utils import __preprocess_get_request, __taco_render, json_response, phone_for_search


class CustomerList(TacoMixin, ListView):
    model = Customer
    template_name = 'taconite/customer/customer_list.xml'

    def get_queryset(self):
        qs = super(CustomerList, self).get_queryset()
        fltr = {}
        if self.request.GET.get('customer_id', None):
            fltr['pk'] = self.request.GET['customer_id']

        if self.request.GET.get('find_customer_name', None):
            fltr['name__icontains'] = self.request.GET['find_customer_name']

        if self.request.GET.get('find_customer_phone', None):
            fltr['telephone_clean__icontains'] = phone_for_search(self.request.GET['find_customer_phone'])

        if self.request.GET.get('find_customer_email', None):
            fltr['email__icontains'] = self.request.GET['find_customer_email']

        if self.request.GET.get('additional_field', None):
            if self.request.GET.get('additional_value', None):
                fltr[self.request.GET['additional_field']] = self.request.GET['additional_value']

        if not fltr:
            if self.request.GET.get('last', None):
                return qs.filter(last_read__isnull=False).order_by('-last_read')[:20]
            else:
                return qs.none()

        return qs.filter(**fltr)


customer_list = CustomerList.as_view()


@login_required
def customer_contact_add(request):
    for obj in serializers.deserialize('json', request.body):
        if obj.object.__class__ == CustomerContact:
            obj.object.slug = None
            obj.object.save()
    return json_response('Contact created')


@login_required
def customer_contact_delete(request, pk):
    try:
        CustomerContact.objects.get(pk=pk).delete()
    except CustomerContact.DoesNotExist:
        return HttpResponse('error')
    return HttpResponse('ok')


@login_required
def customer_note_get(request, c_pk, n_pk=None):
    try:
        c = Customer.objects.get(pk=c_pk)
        if n_pk:
            note = c.notes.get(pk=n_pk)
    except Exception, e:
        return HttpResponse('')

    if request.method == 'POST':
        text = request.POST.get('text', '')
        if not n_pk:
            note = c.notes.create()
        note.text = text
        note.save()

    return __taco_render(request, 'taconite/customer/note.xml', {
        'note': note,
        'customer': c,
        'created': not bool(n_pk)
    })


@login_required
def customer_note_delete(request, c_pk, n_pk):
    try:
        customer = Customer.objects.get(pk=c_pk)
        note = Note.objects.get(pk=n_pk)
    except CustomerContact.DoesNotExist:
        print 'customer not found'
        return HttpResponse('error')

    customer.notes.remove(note)

    return HttpResponse('ok')


@login_required
def customer_get(request, pk):
    pk, params, customer, error = __preprocess_get_request(request, pk, Customer)
    fields = formfields.CustomerForm(customer)
    customer.save()  # update last_read

    only_orders = request.GET.get('only_orders', None)

    return __taco_render(request, 'taconite/customer/customer.xml', {
        'error': error,
        'fields': fields,
        'customer': customer,
        'only_orders': only_orders,
    })


@login_required
def customer_save(request):
    msg = ''
    new_customer = False
    for customer in serializers.deserialize('json', request.body):
        if customer.object.__class__ == Customer:
            if not customer.object.id:
                new_customer = True
                customer.object.set_slug()

            customer.save()

            if new_customer:
                msg = 'Customer created (ID:%d)' % customer.object.id
            else:
                msg = 'Customer saved'
        else:
            msg = 'Did not receive expected object Customer. You sent me a %s' % customer.object.__class__.__name__

    return json_response({
        'msg': msg,
        'customer_id': customer.object.id,
        'creatred': True if new_customer else False
    })
