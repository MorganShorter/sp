from decimal import Decimal
from django.http import HttpResponse
from django.views.generic import ListView
from db_settings.models import Settings as db_s
from ..mixins import MyobMixin
from ..models import Customer, Order


class ServiceSaleList(MyobMixin, ListView):
    model = Order
    fields = (
        'Co./Last Name',
        'First Name',
        'Addr 1 - Line 1',
        '- Line 2',
        '- Line 3',
        '- Line 4',
        'Invoice #',
        'Date',
        'Customer PO',
        'Account #',
        'Amount',
        'Inc-Tax Amount',
        'Tax Code',
        'Non-GST Amount',
        'GST Amount',
        'Freight Amount',
        'Card ID',
        'Record ID'
    )

    def get(self, request, *args, **kwargs):
        ret = ['\t'.join(self.fields)]

        myob_account = db_s.objects.get(key='myob_account').value
        myob_tax_code = db_s.objects.get(key='myob_tax_code').value
        myob_use_addr_only = db_s.objects.get(key='myob_use_addr_only').value
        myob_use_name_in_addr = db_s.objects.get(key='myob_use_name_in_addr').value

        for ob in self.get_queryset():
            data = [
                ob.customer.parsed_name['l'],
                ob.customer.parsed_name['f'],
                '',  # 2 see below
                '',  # 3 ...
                '',  # 4 ...
                '',  # 5 see below
                getattr(ob.last_invoice, 'number', 'no-invoice'),
                ob.order_date.strftime("%d.%m.%Y"),
                ob.id,
                myob_account,
                '$%s' % ob.summary['gross_price'],
                '$%s' % ob.summary['net_price'],
                myob_tax_code,
                '$%s' % ob.summary['gross_price'],
                '$%s' % ob.summary['tax'],
                '$%s' % ob.shipping_cost,
                "*None",
                "*None",
            ]

            if bool(myob_use_addr_only):
                if bool(myob_use_name_in_addr):
                    data[2] = ob.customer.name
                    data[3] = ob.customer.address_line_1
                    data[4] = ob.customer.address_line_2
                else:
                    data[2] = ob.customer.address_line_1
                    data[3] = ob.customer.address_line_2
            else:
                if bool(myob_use_name_in_addr):
                    data[2] = ob.customer.name
                    data[3] = ob.customer.address_line_1
                    data[4] = '%s %s %s' % (ob.customer.suburb, ob.customer.state, ob.customer.postcode)
                    data[5] = ob.customer.address_line_2
                else:
                    data[2] = '%s, %s' % (ob.customer.address_line_1, ob.customer.address_line_2)
                    data[3] = ob.customer.suburb
                    data[4] = ob.customer.state
                    data[5] = ob.customer.postcode

            data = map(lambda x: str(x) if isinstance(x, (int, Decimal)) else x, data)
            ret.append('\t'.join(data))

        return HttpResponse('\n\n'.join(ret), mimetype='text/plain')

service_sale_list = ServiceSaleList.as_view()


class CustomerList(MyobMixin, ListView):
    model = Customer
    fields = (
        'Co./Last Name',
        'First Name',
        'Card ID',
        'Addr 1 - Line 1',
        '- Line 2',
        '- Line 3',
        '- Line 4',
        '- City',
        '- State',
        '- Postcode',
        '- Country',
        '- Phone # 1',
        '- Email',
        '- Contact Name'
    )

    def get(self, request, *args, **kwargs):
        ret = ['\t'.join(self.fields)]

        for ob in self.get_queryset():
            data = [
                ob.parsed_name['l'],
                ob.parsed_name['f'],
                ob.from_src_company_id or "*None",
                ob.address_line_1,
                ob.address_line_2,
                '',
                '',
                ob.suburb,
                ob.state,
                ob.postcode,
                ob.country,
                ob.telephone,
                ob.email,
                ob.contacts_data
            ]
            data = map(lambda x: str(x) if isinstance(x, (int, Decimal)) else x, data)
            ret.append('\t'.join(data))

        return HttpResponse('\n\n'.join(ret), mimetype='text/plain')
customer_list = CustomerList.as_view()