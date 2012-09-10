# mypebble/testimonials/views.py
# MK: 29-Aug-2012

#from django.views.generic import TemplateView
from django.views.generic import DetailView

from mypebble.testimonials.models import Testimonial


class TestimonialView(DetailView):
    template_name = "testimonial.html"
    model = Testimonial
    context_object_name = 'testimonial'
