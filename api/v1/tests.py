#-*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.core.urlresolvers import reverse
from rest_framework import status
import json


class UserDetailAPITest(APITestCase):
    def test_not_found(self):
        url = reverse('v1.user_detail', kwargs={'pk': 999})
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_404_NOT_FOUND)

    def test_found(self):
        user = User.objects.create_user('foo')
        url = reverse('v1.user_detail', kwargs={'pk': user.id})
        r = self.client.get(url)
        self.assertEqual(r.status_code, status.HTTP_200_OK)
        data = json.loads(r.content)
        self.assertEqual(data['username'], 'foo')
