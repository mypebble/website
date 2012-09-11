"""Use the database values from initial_data for the page structure. This is
mostly sanity tests to ensure the website loads the correct pages.
"""
from unittest import skip

from django.test import TestCase, client


@skip('Part of Django CMS, so not really necessary')
class SimplePageTestCase(TestCase):

    fixtures = [
        'core/initial_data.01.json',
        'core/initial_data.02.json',
    ]

    def setUp(self):
        self.client = client.Client()

    def test_home_page(self):
        """Get the home page.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
