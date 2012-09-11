"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from mypebble.testimonials.models import Testimonial


class TestimonialTestCase(TestCase):
    """Confirms that testimonials are correctly displayed in extended form."""

    fixtures = [
        'test_data/testimonials.json',
    ]

    def test_index(self):
        """Checks that the view is accessible in HTTP"""

        response = self.client.get(
            reverse('testimonial-view', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)

    def test_testimonial(self):
        """Check that a testimonial is displayed with correct data."""

        response = self.client.get(
            reverse('testimonial-view', kwargs={'pk': 1}))

        testimonial = response.context['testimonial']

        self.assertEquals(testimonial.pk, 1)
        self.assertEquals(
                testimonial.quote_text, "Testimonial Quote 1")
        self.assertEquals(
                testimonial.quote_text_full, "Full Testimonial Text 1")
