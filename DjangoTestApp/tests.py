# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views

# Create your tests here.

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/home_section/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DjangoTestApp/home_section.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/home_section/')
        self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/home_section/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')

class AboutPageTests(SimpleTestCase):

    def test_about_page_status_code(self):
        response = self.client.get('/about_section/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('about'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'DjangoTestApp/about_section.html')

    def test_about_page_contains_correct_html(self):
        response = self.client.get('/about_section/')
        self.assertContains(response, '<h1>AboutPage</h1>')

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/about_section/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
