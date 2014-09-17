from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', include('transport.urls')),
    url(r'^t/', include('transport.urls')),
    url(r'^admin/chart/$', 'transport.admin_view.chart'),
    url(r'^admin/location_new/(.+)$', 'transport.admin_view.location_new'),
    url(r'^admin/location_his/(.+)$', 'transport.admin_view.location_his'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}),)