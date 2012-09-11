"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""

from django.test import TestCase
from django.core.urlresolvers import reverse

from mypebble.testimonials.models import Testimonial


class TestimonialTestCase(TestCase):
    """Confirms that testimonials are correctly displayed."""

    fixtures = [
        'test_data/testimonials.json',
    ]

    def test_index(self):
        """Checks that the view is accessible in HTTP"""

        response = self.client.get(
            reverse('testimonial-view', kwargs={'pk': 1}))

        self.assertEqual(response.status_code, 200)
