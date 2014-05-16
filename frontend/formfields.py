# { 'selector' : (value, filterchain), ... }
# e.g. { 'input#customer_name': (customer.name, 'upper|make_list|join:-x-') }


def CustomerForm(obj):
    return {
        'input#customer_id': (obj.id, None),
        'input#customer_name': (obj.name, None),
        'input#customer_type': (obj.customer_type, None),
        'input#customer_registration': (obj.registration, 'fix_ampersands'),
        'input#customer_phone': (obj.telephone, None),
        'input#customer_fax': (obj.fax, None),
        'input#customer_email': (obj.email, None),
        'input#customer_address1': (obj.address_line_1, None),
        'input#customer_address2': (obj.address_line_2, None),
        'input#customer_suburb': (obj.suburb, None),
        'select#customer_state': (obj.state, None),
        'input#customer_postcode': (obj.postcode, None),
        'input#customer_country': (obj.country, None),
        'input#customer_delivery_attn': (obj.delivery_attn, None),
        'input#customer_delivery_address1': (obj.delivery_address_line_1, None),
        'input#customer_delivery_address2': (obj.delivery_address_line_2, None),
        'input#customer_delivery_suburb': (obj.delivery_suburb, None),
        'select#customer_delivery_state': (obj.delivery_state, None),
        'input#customer_delivery_postcode': (obj.delivery_postcode, None),
        'input#customer_delivery_country': (obj.delivery_country, None),
        'input#customer_from_src_membadd': (obj.from_src_membadd_id, None),
        'input#customer_from_src_company': (obj.from_src_company_id, None),
        'input#customer_slug': (obj.slug, None)
    }


def OrderForm(order, invoice):
    return {
        '#frm_order .order_id': (order.id, None),
        '#frm_order .customer_id': (order.customer.id, None),
        '#frm_order .order_customer': (order.customer.name, None),
        '#frm_order .order_order_id': (order.id, None),

        '#frm_order .order_order_date': (order.order_date, 'date:d/m/Y'),
        '#frm_order .order_wanted_by': (order.wanted_by, 'date:d/m/Y'),
        '#frm_order .order_shipping_cost': (order.shipping_cost, None),

        '#frm_order .order_invoice_number': (invoice.number, None) if invoice else ('-', None),
        '#frm_order .invoice_company': (invoice.company.id, None) if invoice else ('', None),
    }


def __apply_template_filters(form_fields):
    # Perhaps we should just apply filters here ? rather than use custom templatetag
    pass


def ProductForm(obj):
    return {
        '#frm_product .product_id': (obj.id, None),
        '#frm_product .product_code': (obj.code, None),
        '#frm_product .product_name': (obj.name, None),
        '#frm_product .product_size': (obj.size_id, None),
        '#frm_product .product_type': (obj.type, None),
        '#frm_product .product_cost_price': (obj.sp_cost, None),
        '#frm_product .product_current_stock': (obj.current_stock, None),
        '#frm_product .product_minimum_stock': (obj.minimum_stock, None),
        '#frm_product .product_supplier': (obj.supplier_id, None),
        '#frm_product .product_royalty': (obj.royalty, None),
        '#frm_product .product_medium': (obj.medium_id, None),
    }


def PriceLevelForm(obj):
    return {
        '#frm_add_pricelevel .price_id': (obj.pk, None),
        '#frm_add_pricelevel .pricelevel_min_amount': (obj.min_amount, None),
        '#frm_add_pricelevel .pricelevel_max_amount': (obj.max_amount, 'default_if_none:""'),
        '#frm_add_pricelevel .pricelevel_cost_per_item': (obj.cost_per_item, None),
        '#frm_add_pricelevel .pricelevel_block_only': (obj.block_only, None),
    }