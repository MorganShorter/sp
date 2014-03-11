from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('frontend.views',
    url(ur'^testonite/?', TemplateView.as_view(template_name='taconite/testonite.xml', content_type='text/xml')),
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