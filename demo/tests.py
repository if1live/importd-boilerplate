#-*- coding: utf-8 -*-

from django.test import TestCase
from django.core.urlresolvers import reverse
import json


class DemoViewTest(TestCase):
    def test_run(self):
        url_list = [
            reverse('demo.index'),
            reverse('demo.filters_jinja2'),
        ]
        for url in url_list:
            r = self.client.get(url)
            self.assertEqual(200, r.status_code)

    def test_param_url(self):
        url = reverse('demo.param_url', kwargs={'foo': 1, 'bar': 2})
        r = self.client.get(url)
        data = json.loads(r.content)
        self.assertEqual(data['foo'], 1)
        self.assertEqual(data['bar'], 2)

