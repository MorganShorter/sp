from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^testonite/?', TemplateView.as_view(template_name='taconite/testonite.xml', content_type='text/xml')),

    url(ur'^lookup/states/?', 'ajax_lookup_states'),

    url(ur'^customer/save/?(?P<pk>\d*)', 'customer_save'),
    url(ur'^customer/delete/?(?P<pk>\d*)', 'customer_delete'),
    url(ur'^customer/?(?P<pk>\d*)', 'customer_get'),

    url(ur'^order/?(?P<pk>\d*)', 'order_get'),
)

urlpatterns += patterns('',
    # Examples:
    # url(r'^$', 'sp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url('', TemplateView.as_view(template_name='base.html'))
)
