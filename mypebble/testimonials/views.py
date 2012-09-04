# mypebble/testimonials/views.py
# MK: 29-Aug-2012

#from django.views.generic import TemplateView
from django.views.generic import DetailView

from cmsplugin_randomquote.models import Quote


class TestimonialView(DetailView):
    template_name = "testimonial.html"
    model = Quote
    context_object_name = 'testimonial'
