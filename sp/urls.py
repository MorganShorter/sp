from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('frontend.views',
    #url(r'^customer/(?P<id>\d+)/$', 'customer_detail'),
    url(r'^customer/(?P<customer_id>\d+)/#?$', 'customer_detail'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'sp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('','django.views.generic.simple.direct_to_template', {'template': 'base.html', 'mimetype': 'text/html'}),
)
