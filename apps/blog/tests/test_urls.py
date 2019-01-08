from django.test import SimpleTestCase
from django.urls import reverse, resolve

from ..views import index, series, tags, about

class TestUrls(SimpleTestCase):

	def test_index_url_resolves_index_view(self):
		url = reverse('index')
		self.assertEquals(resolve(url).func, index)

	def test_series_url_resolves_series_view(self):
		url = reverse('series')
		self.assertEquals(resolve(url).func, series)

	def test_tags_url_resolves_tags_view(self):
		url = reverse('tags')
		self.assertEquals(resolve(url).func, tags)

	def test_about_url_resolves_url_view(self):
		url = reverse('about')
		self.assertEquals(resolve(url).func, about)
