from django.db import models

class VideoGame(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)
	img = models.ImageField(upload_to='images/videogames/')
	category = models.CharField(max_length=50)
	launch = models.DateField()
	website = models.URLField(blank=True, null=True)
	description = models.TextField()

	def __str__(self):
		return self.name

class Team(models.Model):
	name = models.CharField(max_length=30)
	slug = models.SlugField(max_length=40, unique=True)
	img = models.ImageField(upload_to='images/teams/')
	website = models.URLField(blank=True, null=True)
	description = models.TextField()
	videogames = models.ManyToManyField(
		VideoGame,
		related_name='teams',
	)
	def __str__(self):
		return self.name

class Gamer(models.Model):
	nickname = models.CharField(max_length=30)
	slug = models.SlugField(max_length=50, unique=True)
	name = models.CharField(max_length=50)
	birth = models.DateField()
	img = models.ImageField(upload_to='images/gamers/')
	description = models.TextField()
	country = models.CharField(max_length=30)
	team = models.ForeignKey(
		Team,
		related_name='members',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	videogames = models.ManyToManyField(
		VideoGame,
		related_name='gamers',
	)
	def __str__(self):
		return self.nickname
