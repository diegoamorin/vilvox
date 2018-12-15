from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
	subject = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.subject

class List(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120,unique=True)
	description = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to='images/list/')

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to='images/post/')
	series = models.ForeignKey(
		List, 
		related_name='posts',
		on_delete=models.CASCADE,
		blank=True,
		null=True,
	)
	tags = models.ManyToManyField(
		Tag,
		related_name='posts',
	)

	def __str__(self):
		return self.title
