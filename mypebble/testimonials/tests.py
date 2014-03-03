from django.test import TestCase
from django.core.urlresolvers import reverse

from mypebble.testimonials.models import Testimonial


class TestimonialTestCase(TestCase):
    """Confirms that testimonials are correctly displayed in extended form."""

    def setUp(self):
        """Manually loading the fixtures because CircleCI isn't going to load
        them.
        """
        self.testimonial = Testimonial(
            quote_text='Testimonial Quote 1',
            author='Author 1',
            quote_text_full='Full Testimonial Text 1.')
        self.testimonial.save()

        Testimonial.objects.create(
            quote_text='Testimonial Quote 2',
            author='Author 2',
            quote_text_full='Full Testimonial Text 2.')
        Testimonial.objects.create(
            quote_text='Testimonial Quote 3',
            author='Author 3',
            quote_text_full='Full Testimonial Text 3.')

    def test_index(self):
        """Checks that the view is accessible in HTTP"""
        response = self.client.get(
            reverse('testimonial-view', kwargs={'pk': self.testimonial.pk}))

        self.assertEqual(response.status_code, 200)

    def test_testimonial(self):
        """Check that a testimonial is displayed with correct data."""

        response = self.client.get(
            reverse('testimonial-view', kwargs={'pk': self.testimonial.pk}))

        testimonial = response.context['testimonial']

        self.assertEquals(testimonial.pk, self.testimonial.pk)
        self.assertEquals(
                testimonial.quote_text, "Testimonial Quote 1")
        self.assertEquals(
                testimonial.quote_text_full, "Full Testimonial Text 1.")
