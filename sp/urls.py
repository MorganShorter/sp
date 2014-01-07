from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    #url(r'^customer/(?P<id>\d+)/$', 'customer_detail'),
    url(r'^customer/(?P<customer_id>\d+)/?#?$', 'customer_detail'),
    url(r'^order/(?P<order_id>\d+)/?#?$', 'order_detail'),
    url(r'^lookup/states', 'ajax_lookup_states'),
    url(r'^lookup/customer', 'ajax_lookup_customer'),
    url(r'^save/customer', 'ajax_save_customer'),
    url(r'^lookup/order', 'ajax_lookup_order'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'sp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('','django.views.generic.simple.direct_to_template', {'template': 'base.html', 'mimetype': 'text/html'}),
)
