from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

from django.conf.urls.defaults import patterns, include, url
import forms_builder.forms.urls # add this import


from cms.sitemaps import CMSSitemap

admin.autodiscover()

from mypebble.testimonials.views import TestimonialView
from mypebble.core.views import contact

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),

    url(r'^forms/', include('forms_builder.forms.urls')),

    url(r'^testimonial/(?P<pk>\d+)/$', TestimonialView.as_view(),
        name='testimonial-view'),
    url(r'^enquiries/$', contact,
        name='enquiry-form-general'),
    url(r'^enquiries/(?P<form_type>\w+)/$', contact,
        name='enquiry-form-specific'),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),

    url(r'^admin/', include(admin.site.urls)),


    #url(r'^weblog/', include('zinnia.urls')),
    #url(r'^comments/', include('django.contrib.comments.urls')),

#        url(r'', include('django.contrib.staticfiles.urls')),
    ) + urlpatterns

#urlpatterns += staticfiles_urlpatterns()


