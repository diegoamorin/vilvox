from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

	def setUp(self):
		self.client = Client()
		self.index_url = reverse('index')
		self.series_url = reverse('series')
		self.tags_url = reverse('tags')
		self.about = reverse('about')

	def test_index_view_status_code(self):
		response = self.client.get(self.index_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'index.html')

	def test_series_view_status_code(self):
		response = self.client.get(self.series_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'series.html')

	def test_tags_view_status_code(self):
		response = self.client.get(self.tags_url)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'tags.html')

	def test_about_view_status_code(self):
		response = self.client.get(self.about)

		self.assertEquals(response.status_code, 200)
		self.assertTemplateUsed(response, 'about.html')
