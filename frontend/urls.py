from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^$', 'index_entry', name='index'),
    url(ur'^lookup/states/?', 'ajax_lookup_states'),
    url(ur'^lookup/size/?', 'ajax_lookup_size'),
    url(ur'^lookup/supplier/?', 'ajax_lookup_supplier'),
    url(ur'^lookup/medium/?', 'ajax_lookup_medium'),
    url(ur'^lookup/royalty_group/?', 'ajax_lookup_royalty_group'),
    url(ur'^lookup/company/?', 'ajax_lookup_company'),
    url(ur'^lookup/order/status/?', 'ajax_lookup_order_status'),
    url(ur'^lookup/catalog/?', 'ajax_lookup_catalog'),
)

# Order
urlpatterns += patterns('frontend.views.order',
    url(ur'^order/save/', 'order_save'),
    url(ur'^order/list/', 'order_list', name='order_list'),
    url(ur'^order/get/(?P<pk>\d*)/', 'order_get'),
    url(ur'^order/get_pdf/(?P<pk>\d*)/', 'order_get', {'pdf': True}),
    url(ur'^order/send_pdf/(?P<pk>\d*)/', 'order_get', {'pdf': True, 'send_mail': True}),
    url(ur'^order/create/(?P<customer_pk>\d*)/', 'order_create'),
    url(ur'^order/delete/(?P<pk>\d*)/', 'order_delete'),

    # product in order
    url(ur'^order/add_product/(?P<order_id>\d+)/(?P<product_id>\d+)/', 'order_add_product'),
    url(ur'^order/delete_product/(?P<order_product_id>\d+)/', 'order_delete_product'),

)

# Product
urlpatterns += patterns('frontend.views.product',
    url(ur'^product/save/', 'product_save'),
    url(ur'^product/list/', 'product_list', name='product_list'),
    url(ur'^product/(?P<pk>\d*)/', 'product_get', name='product_get'),

    url(ur'^product/pricelevel/save/', 'product_price_save'),
    url(ur'^product/pricelevel/(?P<prod_id>\d*)/?(?P<price_id>\d*)/delete/', 'product_price_delete'),
    url(ur'^product/pricelevel/(?P<prod_id>\d*)/?(?P<price_id>\d*)/', 'product_price_get'),

    url(ur'^product/issue/save/', 'product_issue_save'),
    url(ur'^product/issue/(?P<prod_id>\d*)/?(?P<issue_id>\d*)/delete/', 'product_issue_delete'),
    url(ur'^product/issue/(?P<prod_id>\d*)/?(?P<issue_id>\d*)/', 'product_issue_get'),

    url(ur'^product/stock_adjust/(?P<prod_id>\d*)/', 'product_stock_adjust'),
)

# Customer
urlpatterns += patterns('frontend.views.customer',
    url(ur'^customer/save/', 'customer_save'),
    url(ur'^customer/list/', 'customer_list', name='customer_list'),
    url(ur'^customer/note/(?P<c_pk>\d*)/?(?P<n_pk>\d*)/delete/', 'customer_note_delete'),
    url(ur'^customer/note/(?P<c_pk>\d*)/?(?P<n_pk>\d*)/', 'customer_note_get'),
    url(ur'^customer/(?P<pk>\d*)/', 'customer_get'),

    # Contact
    url(ur'^contact/add/', 'customer_contact_add', name='contact_add'),
    url(ur'^contact/delete/?(?P<pk>\d*)', 'customer_contact_delete'),
)

# Report
urlpatterns += patterns('frontend.views.reports',
    url(ur'^report/1/get/', 'report_1', name='report_1'),
    url(ur'^report/2/get/', 'report_2', name='report_2'),
    url(ur'^report/3/get/', 'report_3', name='report_3'),
    url(ur'^report/4/get/', 'report_4', name='report_4'),
    url(ur'^report/5/get/', 'report_5', name='report_5'),
    url(ur'^report/6/get/', 'report_6', name='report_6'),
    url(ur'^report/7/get/', 'report_7', name='report_7'),
)

# Royalty Group CRUD
urlpatterns += patterns('frontend.views.royalty',
    url(ur'^royalty/save/', 'obj_save'),
    url(ur'^royalty/list/', 'obj_list', name='royalty_list'),
    url(ur'^royalty/open/(?P<pk>\d*)/', 'obj_get', name='royalty_get'),
    url(ur'^royalty/delete/(?P<pk>\d*)/', 'obj_delete'),
)

# Size CRUD
urlpatterns += patterns('frontend.views.size',
    url(ur'^size/save/', 'obj_save'),
    url(ur'^size/list/', 'obj_list', name='size_list'),
    url(ur'^size/open/(?P<pk>\d*)/', 'obj_get', name='size_get'),
    url(ur'^size/delete/(?P<pk>\d*)/', 'obj_delete'),
)

# Medium CRUD
urlpatterns += patterns('frontend.views.medium',
    url(ur'^medium/save/', 'obj_save'),
    url(ur'^medium/list/', 'obj_list', name='medium_list'),
    url(ur'^medium/open/(?P<pk>\d*)/', 'obj_get', name='medium_get'),
    url(ur'^medium/delete/(?P<pk>\d*)/', 'obj_delete'),
)

# Supplier CRUD
urlpatterns += patterns('frontend.views.supplier',
    url(ur'^supplier/save/', 'obj_save'),
    url(ur'^supplier/list/', 'obj_list', name='supplier_list'),
    url(ur'^supplier/open/(?P<pk>\d*)/', 'obj_get', name='supplier_get'),
    url(ur'^supplier/delete/(?P<pk>\d*)/', 'obj_delete'),
)

# Catalog CRUD
urlpatterns += patterns('frontend.views.catalog',
    url(ur'^catalog/save/', 'obj_save'),
    url(ur'^catalog/list/', 'obj_list', name='catalog_list'),
    url(ur'^catalog/open/(?P<pk>\d*)/', 'obj_get', name='catalog_get'),
    url(ur'^catalog/delete/(?P<pk>\d*)/', 'obj_delete'),

    url(ur'^catalog/issue/save/', 'obj_issue_save'),
    url(ur'^catalog/issue/open/(?P<pk>\d*)/', 'obj_issue_get'),
    url(ur'^catalog/issue/delete/(?P<pk>\d*)/', 'obj_issue_delete'),
)

# BO CRUD
urlpatterns += patterns('frontend.views.bo',
    url(ur'^bo/update/', 'obj_update'),
    url(ur'^bo/list/', 'obj_list', name='bo_list'),
)

# MYOB Export
urlpatterns += patterns('frontend.views.myob',
    url(ur'^myob_export/service_sale/', 'service_sale_list'),
    url(ur'^myob_export/customer/', 'customer_list'),
)