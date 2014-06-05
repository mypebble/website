"""Tests for the core pieces of the website. This does not include the CMS,
which is tested by Django CMS themselves.
"""
from unittest import skip

from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase, client


class GeneralEnquiryTestCase(TestCase):
    """Tests to ensure we can send emails when the user fills out an enquiries
    form
    """
    def setUp(self):
        self.client = client.Client()

    def test_post_form(self):
        """Test General
        """
        response = self.client.post(
          reverse('enquiry-form-general'),
          {
            'name': 'a name',
            'email': 'ah@talktopebble.co.uk',
            'organisation': 'a organisation',
            'postcode': 'aa1-11a',
            'telephone': '0123456',
            'message': 'a message',
          }
        )


        self.assertEqual(response.status_code, 200)
