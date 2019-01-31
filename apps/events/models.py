from django.db import models

from ..wiki.models import VideoGame, Team

class Event(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	description = models.TextField()
	start_day = models.DateField()
	end_day = models.DateField(blank=True, null=True)
	img = models.ImageField(upload_to='images/events/')

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

	def __str__(self):
		return self.slug
