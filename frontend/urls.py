from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^lookup/states/?', 'ajax_lookup_states'),

    # Customer
    url(ur'^customer/save/?(?P<pk>\d*)', 'customer_save'),
    url(ur'^customer/list/', 'customer_list', name='customer_list'),
    url(ur'^customer/note/(?P<c_pk>\d*)/?(?P<n_pk>\d*)/delete/', 'customer_note_delete'),
    url(ur'^customer/note/(?P<c_pk>\d*)/?(?P<n_pk>\d*)/', 'customer_note_get'),
    url(ur'^customer/(?P<pk>\d*)/', 'customer_get'),

    # Order
    url(ur'^order/?(?P<pk>\d*)', 'order_get'),

    # Contact
    url(ur'^contact/add/', 'contact_add', name='contact_add'),
    url(ur'^contact/delete/?(?P<pk>\d*)', 'contact_delete'),
)


urlpatterns += patterns('frontend.views.reports',
    # Report
    url(ur'^report/1/get/', 'report_1', name='report_1'),
    url(ur'^report/2/get/', 'report_2', name='report_2'),
    url(ur'^report/3/get/', 'report_3', name='report_3'),
)
