from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'homepage.html'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'', include('staticfiles.urls')),
    )

