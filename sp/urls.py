from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^testonite/?', TemplateView.as_view(template_name='taconite/testonite.xml', content_type='text/xml')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'', include('frontend.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# For development only
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {"document_root": settings.MEDIA_ROOT}),
    )