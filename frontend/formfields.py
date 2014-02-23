# { 'selector' : (value, filterchain), ... }
# e.g. { 'input#customer_name': (customer.name, 'upper|make_list|join:-x-') }
def CustomerForm(customer):
    return { 'input#customer_id': (customer.id, None),
             'input#customer_name': (customer.name, None),
             'input#customer_type': (customer.customer_type, None),
             'input#customer_registration': (customer.registration, 'fix_ampersands'),
             'input#customer_phone': (customer.telephone, None),
             'input#customer_fax': (customer.fax, None),
             'input#customer_email': (customer.email, None),
             'input#customer_address1': (customer.address_line_1, None),
             'input#customer_address2': (customer.address_line_2, None),
             'input#customer_suburb': (customer.suburb, None),
             'select#customer_state': (customer.state, None),
             'input#customer_postcode': (customer.postcode, None),
             'input#customer_country': (customer.country, None),
             'input#customer_delivery_attn': (customer.delivery_attn, None),
             'input#customer_delivery_address1': (customer.delivery_address_line_1, None),
             'input#customer_delivery_address2': (customer.delivery_address_line_2, None),
             'input#customer_delivery_suburb': (customer.delivery_suburb, None),
             'select#customer_delivery_state': (customer.delivery_state, None),
             'input#customer_delivery_postcode': (customer.delivery_postcode, None),
             'input#customer_delivery_country': (customer.delivery_country, None),
             'input#customer_from_src_membadd': (customer.from_src_membadd_id, None),
             'input#customer_from_src_company': (customer.from_src_company_id, None),
             'input#customer_slug': (customer.slug, None)}


def OrderForm(order, invoice):
    return { 'input#order_order_id': (order.id, None),
             'input#order_customer_id': (order.customer.id, None),
             'input#order_invoice_number': (invoice.number, 'date:d/m/Y'),
             'input#order_order_date': (order.order_date, 'date:d/m/Y'),
             'input#order_order_company': (invoice.company.name, None),
             'input#order_wanted_by': (order.wanted_by, 'date:d/m/Y'),
             'input#order_shipping_cost': (order.shipping_cost, None) }

def __apply_template_filters(form_fields):
    # Perhaps we should just apply filters here ? rather than use custom templatetag
    pass
