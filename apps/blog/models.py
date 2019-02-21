from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from markdownx.models import MarkdownxField

# class UserProfile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	avatar = models.ImageField('images/profiles/')
# 	bio = models.TextField(max_length=500, blank=True)
# 	location = models.CharField(max_length=30, blank=True)
# 	birth_date = models.DateField(null=True, blank=True)

class Tag(models.Model):
	subject = models.CharField(max_length=20, unique=True)
	slug = models.SlugField(unique=True, max_length=20, null=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.subject)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.subject

class List(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=120, unique=True)
	description = models.TextField()
	last_update = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(upload_to='images/list/')

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

class Post(models.Model):
	title = models.CharField(max_length=100)
	# author = models.ForeignKey(UserProfile, related_name='posts')
	slug = models.SlugField(max_length=120, unique=True)
	content = MarkdownxField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(null=True)
	img = models.ImageField(upload_to='images/post/')
	series = models.ManyToManyField(
		List,
		related_name='posts',
		blank=True,
	)
	tags = models.ManyToManyField(
		Tag,
		related_name='posts',
	)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

class CDNImage(models.Model):
	img = models.ImageField(upload_to='images/CDNImages/')
