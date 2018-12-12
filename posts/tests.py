# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.test import TestCase
from django.urls import reverse

from .models import Posts


class PostsTests(TestCase):

    def setUp(self):
        Posts.objects.create(text='just a test')

    def test_text_content(self):
        posts = Posts.objects.get(id=1)
        expected_object_name = posts.text
        self.assertEquals(expected_object_name, 'just a test')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'DjangoTestApp/posts.html')