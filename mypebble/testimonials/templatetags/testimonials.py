# Custom template tags

from cmsplugin_randomquote.models import Quote
from django import template

register = template.Library()


class Testimonials(template.Node):
    def render(self, context):
        try:
            t_obj = Quote.objects.order_by('?')[0:3]
            context['quotes'] = t_obj
        except IndexError:
            pass

        doc = template.loader.get_template('testimonials_frag.html')

        return doc.render(context)


@register.tag
def testimonials(*args, **kwargs):
    return Testimonials()
