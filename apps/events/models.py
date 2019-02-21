from django.db import models
from django.template.defaultfilters import slugify

from ..wiki.models import VideoGame, Team

class Event(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	description = models.TextField()
	start_day = models.DateField()
	end_day = models.DateField(blank=True, null=True)
	img = models.ImageField(upload_to='images/events/')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

class Game(models.Model):
	slug = models.SlugField(max_length=120, unique=True)
	day = models.DateTimeField()

	videogame = models.ForeignKey(
		VideoGame,
		related_name='games',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	teams = models.ManyToManyField(
		Team,
		related_name='games',
	)
	event = models.ForeignKey(
		Event,
		related_name="games",
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)

	def generate_slug(day):
		import random
		import string

		letras = string.ascii_letters
		letras = [i for i in letras]
		conjunto = ['1', '2', '3', '4', '5', '6', '7', '8', '9', *letras]
		result = []

		for _ in range(5):
			result.append(random.choice(conjunto))

		return "".join(result)

	def save(self, *args, **kwargs):
		new_string = str(self.day.date()) + ' game ' + self.generate_slug()
		self.slug = slugify(new_string)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.slug
