#-*- coding: utf-8 -*-

from django.test import TestCase

class SimpleViewTest(TestCase):
    def test_run(self):
        r = self.client.get('/')
        self.assertEqual(200, r.status_code)
