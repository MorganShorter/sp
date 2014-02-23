from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^testonite/?', TemplateView.as_view(template_name='taconite/testonite.xml', content_type='text/xml')),
    url(ur'^lookup/states/?', 'ajax_lookup_states'),

    url(ur'^customer/save/?(?P<pk>\d*)', 'customer_save'),
    #url(ur'^customer/delete/?(?P<pk>\d*)', 'customer_delete'),
    url(ur'^customer/list/', 'customer_list', name='customer_list'),
    url(ur'^customer/?(?P<pk>\d*)', 'customer_get'),

    url(ur'^order/?(?P<pk>\d*)', 'order_get'),

    url(ur'^contact/add/', 'contact_add', name='contact_add'),

)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url('', TemplateView.as_view(template_name='base.html'))
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# For development only
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
    )