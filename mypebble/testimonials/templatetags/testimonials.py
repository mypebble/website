# Custom template tags

#from cmsplugin_randomquote.models import Quote
from mypebble.testimonials.models import Testimonial
from django import template

register = template.Library()


class Testimonials(template.Node):
    """Renders three testimonials at random from model."""

    def render(self, context):
        try:
            quotes = Testimonial.objects.order_by('?')[0:3]
            context['quotes'] = quotes

        except IndexError:
            pass

        doc = template.loader.get_template('testimonials_frag.html')

        return doc.render(context)


@register.tag
def testimonials(*args, **kwargs):
    return Testimonials()
