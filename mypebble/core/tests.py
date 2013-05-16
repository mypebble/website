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
            'interested': [
              'FM','SFF',
            ],
            'wouldlike': [
              'demo','onsite/demo','other',
            ]
          }
        )

    def test_post_form_specific_period_end(self):
        """Test Training Form Period End
        """
        kwargs = {'form_type': 'training_period_end'}
        response = self.client.post(
          reverse('enquiry-form-specific', kwargs=kwargs),
          {
            'name': 'a name',
            'email': 'ah@talktopebble.co.uk',
            'organisation': 'a organisation',
            'telephone': '0123456',
            'training': [
              'August PE',
            ]
          }
        )

    def test_post_form_specific_groups(self):
        """Test Training Form Groups
        """
        kwargs = {'form_type': 'training_group'}
        response = self.client.post(
          reverse('enquiry-form-specific', kwargs=kwargs),
          {
            'name': 'a name',
            'email': 'ah@talktopebble.co.uk',
            'organisation': 'a organisation',
            'telephone': '0123456',
            'training': [
              'Wed 22 May','Wed 05 June','Keep Updated',
            ]
          }
        )

    def test_post_form_specific_not_paid(self):
        """Test Training Form Not Paid
        """
        kwargs = {'form_type': 'training_not_paid'}
        response = self.client.post(
          reverse('enquiry-form-specific', kwargs=kwargs),
          {
            'name': 'a name',
            'email': 'ah@talktopebble.co.uk',
            'organisation': 'a organisation',
            'telephone': '0123456',
            'training': [
              'Wed 22 May','Wed 05 June','Keep Updated',
            ]
          }
        )
    def test_post_form_specific_new_features(self):
        """Test Training Form New Features
        """
        kwargs = {'form_type': 'training_new_features'}
        response = self.client.post(
          reverse('enquiry-form-specific', kwargs=kwargs),
          {
            'name': 'a name',
            'email': 'ah@talktopebble.co.uk',
            'organisation': 'a organisation',
            'telephone': '0123456',
            'training': [
              'Thur 23 May','Thur 06 June','Keep Updated',
            ]
          }
        )        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].is_valid(), True)
        self.assertEqual(len(mail.outbox), 1)
