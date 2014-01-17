def CustomerForm(customer):
    return { 'input#customer_id': customer.id,
             'input#customer_name': customer.name,
             'input#customer_type': customer.customer_type,
             'input#customer_registration': customer.registration,
             'input#customer_phone': customer.telephone,
             'input#customer_fax': customer.fax,
             'input#customer_email': customer.email,
             'input#customer_address1': customer.address_line_1,
             'input#customer_address2': customer.address_line_2,
             'input#customer_suburb': customer.suburb,
             'select#customer_state': customer.state,
             'input#customer_postcode': customer.postcode,
             'input#customer_country': customer.country,
             'input#customer_delivery_attn': customer.delivery_attn,
             'input#customer_delivery_address1': customer.delivery_address_line_1,
             'input#customer_delivery_address2': customer.delivery_address_line_2,
             'input#customer_delivery_suburb': customer.delivery_suburb,
             'select#customer_delivery_state': customer.delivery_state,
             'input#customer_delivery_postcode': customer.delivery_postcode,
             'input#customer_delivery_country': customer.delivery_country,
             'input#customer_from_src_membadd': customer.from_src_membadd_id,
             'input#customer_from_src_company': customer.from_src_company_id,
             'input#customer_slug': customer.slug }

def OrderForm(order, invoice):
    return { }
