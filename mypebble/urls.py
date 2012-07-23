from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from django.conf.urls.defaults import patterns, include, url
import forms_builder.forms.urls # add this import

from django.contrib import admin
admin.autodiscover()



from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
            
    url(r'^admin/', include(admin.site.urls)),
    url(r'^forms/', include(forms_builder.forms.urls)),
            
#        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

urlpatterns += staticfiles_urlpatterns()


