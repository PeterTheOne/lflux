from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.conf import settings
from ladmin.admin import admin
from django.contrib import admin as adminadmin
adminadmin.autodiscover()

urlpatterns = patterns(
    '',

    url('^$', 'lstory.views.index'),

    url('^story/', include('lfluxproject.lstory.urls')),
    url('^story/', include('lfluxproject.lqa.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(adminadmin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    url(r'^backend/', include(admin.urls)),

    url(r'^api/tumblelog/', include('tumblelog.urls', namespace='tumblelog')),
    url(r'^api/comments/', include('django.contrib.comments.urls')),
    url(r'^api/voting/', include('voting.urls')),

    url(r'^accounts/', include('userena.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )

urlpatterns += patterns('', url(r'^(?P<url>.*)$', 'django.contrib.flatpages.views.flatpage'),)
