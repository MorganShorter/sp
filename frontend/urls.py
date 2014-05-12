from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^lookup/states/?', 'ajax_lookup_states'),
    url(ur'^lookup/size/?', 'ajax_lookup_size'),
    url(ur'^lookup/supplier/?', 'ajax_lookup_supplier'),
    url(ur'^lookup/royalty_img/?', 'ajax_lookup_royalty_img'),
    url(ur'^lookup/medium/?', 'ajax_lookup_medium'),

    # Order
    url(ur'^order/?(?P<pk>\d*)', 'order_get'),

)

# Product
urlpatterns += patterns('frontend.views.product',
    url(ur'^product/save/', 'product_save'),
    url(ur'^product/list/', 'product_list', name='product_list'),
    url(ur'^product/(?P<pk>\d*)/', 'product_get', name='product_get'),
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