# mypebble/testimonials/views.py
# MK: 29-Aug-2012

from django.views.generic import TemplateView


class TestimonialsView(TemplateView):
    template_name = "testimonials.html"
