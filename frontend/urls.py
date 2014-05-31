from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^$', 'index_entry', name='index'),
    url(ur'^lookup/states/?', 'ajax_lookup_states'),
    url(ur'^lookup/size/?', 'ajax_lookup_size'),
    url(ur'^lookup/supplier/?', 'ajax_lookup_supplier'),
    url(ur'^lookup/royalty_img/?', 'ajax_lookup_royalty_img'),
    url(ur'^lookup/medium/?', 'ajax_lookup_medium'),
    url(ur'^lookup/price_level_group/?', 'ajax_lookup_price_level_group'),
    url(ur'^lookup/company/?', 'ajax_lookup_company'),
    url(ur'^lookup/order/status/?', 'ajax_lookup_order_status'),

)

# Order
urlpatterns += patterns('frontend.views.order',
    url(ur'^order/save/', 'order_save'),
    url(ur'^order/list/', 'order_list', name='order_list'),
    url(ur'^order/get/(?P<pk>\d*)/', 'order_get'),
    url(ur'^order/create/(?P<customer_pk>\d*)/', 'order_create'),
    url(ur'^order/delete/(?P<pk>\d*)/', 'order_delete'),

    # product in order
    url(ur'^order/add_product/(?P<order_id>\d+)/(?P<product_id>\d+)/', 'order_add_product'),
    url(ur'^order/delete_product/(?P<order_id>\d+)/(?P<product_id>\d+)/', 'order_delete_product'),

)

# Product
urlpatterns += patterns('frontend.views.product',
    url(ur'^product/save/', 'product_save'),
    url(ur'^product/list/', 'product_list', name='product_list'),
    url(ur'^product/(?P<pk>\d*)/', 'product_get', name='product_get'),

    url(ur'^product/pricelevel/save/', 'product_price_save'),
    url(ur'^product/pricelevel/(?P<prod_id>\d*)/?(?P<price_id>\d*)/delete/', 'product_price_delete'),
    url(ur'^product/pricelevel/(?P<prod_id>\d*)/?(?P<price_id>\d*)/', 'product_price_get'),

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
)

# Price Level Group CRUD
urlpatterns += patterns('frontend.views.level',
    url(ur'^price_level/save/', 'obj_save'),
    url(ur'^price_level/list/', 'obj_list', name='level_list'),
    url(ur'^price_level/open/(?P<pk>\d*)/', 'obj_get', name='level_get'),
    url(ur'^price_level/delete/(?P<pk>\d*)/', 'obj_delete'),
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