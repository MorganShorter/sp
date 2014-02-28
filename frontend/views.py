import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.http import HttpResponse
from django.core import serializers
from django.template import loader, RequestContext

from . import formfields
from .models import Customer, Order, Invoice, CustomerContact
from .mixins import TacoMixin


class CustomerList(TacoMixin, ListView):
    model = Customer
    template_name = 'taconite/customer_list.xml'

    def get_queryset(self):
        qs = super(CustomerList, self).get_queryset()
        fltr = {}
        if self.request.GET.get('customer_id', None):
            fltr['pk'] = self.request.GET['customer_id']

        if self.request.GET.get('find_customer_name', None):
            fltr['name__icontains'] = self.request.GET['find_customer_name']

        if self.request.GET.get('find_customer_phone', None):
            fltr['telephone__icontains'] = self.request.GET['find_customer_phone']

        if self.request.GET.get('find_customer_email', None):
            fltr['email__icontains'] = self.request.GET['find_customer_email']

        if not fltr:
            return qs.none()

        return qs.filter(**fltr)


customer_list = CustomerList.as_view()


def contact_add(request):
    for obj in serializers.deserialize('json', request.body):
        if obj.object.__class__ == CustomerContact:
            obj.object.slug = None
            obj.object.save()
    return HttpResponse(json.dumps('Contact created'), content_type='application/json')


def contact_delete(request, pk):
    try:
        CustomerContact.objects.get(pk=pk).delete()
    except CustomerContact.DoesNotExist:
        print 'contact not found'

    return HttpResponse('ok')

def customer_note_get(request, c_pk, n_pk):
    try:
        c = Customer.objects.get(pk=c_pk)
        note = c.notes.get(pk=n_pk)
    except Exception, e:
        return HttpResponse('')

    if request.method == 'POST':
        text = request.POST.get('text', '')
        note.text = text
        note.save()

    return __taco_render(request, 'taconite/note.xml', {'note': note, 'customer': c})

'''
 Old code
'''

def order_get(request, pk):
    pk, params, order, error = __preprocess_get_request(request, pk, Order)
    invoice = Invoice()

    if not error:
        try:
            invoice = Invoice.objects.filter(order_id=order.id).first()
        except Invoice.DoesNotExist:
            pass

    fields = formfields.OrderForm(order, invoice)
    return __taco_render(request, 'taconite/order.xml', {'error':error, 'fields': fields, 'order': order})


def customer_get(request, pk):
    pk, params, customer, error = __preprocess_get_request(request, pk, Customer)
    fields = formfields.CustomerForm(customer)
    return __taco_render(request, 'taconite/customer.xml', {'error': error, 'fields': fields, 'customer': customer})





def customer_save(request, pk):
    print request.body
    print request.body.__class__.__name__
    for customer in serializers.deserialize('json', request.body):
        print customer
        print customer.object
        if customer.object.__class__ == Customer:
            if not customer.object.id:
                new_customer = True
                customer.object.slug = None
            else:
                new_customer = False

            customer.save()

            if new_customer:
                msg = 'Customer created (ID:%d)' % customer.object.id
            else:
                msg = 'Customer saved'
        else:
            msg = 'Did not receive expected object Customer. You sent me a %s' % customer.object.__class__.__name__

    return HttpResponse(json.dumps(msg), content_type='application/json')


def __preprocess_get_request(request, pk, model):
    error = None
    obj = None

    if request.method == 'POST':
        params = request.POST
    elif request.method == 'GET':
        params = request.GET
    else:
        params = {}

    if not pk and params.has_key('id'):
        pk = params['id']

    if pk:
        try:
            obj = model.objects.get(pk=pk)
        except model.DoesNotExist:
            error = 'No %s found with id %s' % (model.__class__.__name__, pk)
    else:
        error = 'No primary key given to find %s' % model.__class__.__name__

    return pk, params, obj, error


def __taco_render(request, template, context):
    taco_controlplate = loader.get_template(template)
    c_royal = RequestContext(request, context)
    return HttpResponse(taco_controlplate.render(c_royal), content_type='application/xml')


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

    return HttpResponse(json.dumps(states), content_type='application/json')

