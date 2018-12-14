from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	description = models.TextField()
	start_day = models.DateField()
	end_day = models.DateField()
	img = models.ImageField(upload_to='images/events/')

	def __str__(self):
		return self.name

class Game(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	day = models.DateTimeField()

	STATE_CHOICES = (
		('EN_ESPERA', 'En Espera'),
		('EN_JUEGO', 'En Juego'),
		('TERMINADO','Terminado'),
	)
	state = models.CharField(
		max_length=30, 
		choices=STATE_CHOICES, 
		default='EN_ESPERA',
	)

	events = models.ForeignKey(
		Event,
		related_name="games",
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)

	def __str__(self):
		return self.name
