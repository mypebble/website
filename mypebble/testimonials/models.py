from django.db import models

from cmsplugin_randomquote.models import Quote


class Testimonial(Quote):
    quote_text_full = models.TextField()

    class Meta:
        app_label = 'testimonials'
