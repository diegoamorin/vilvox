from django.db import models
from django.template.defaultfilters import slugify

from ..blog.models import SocialURL


class VideoGame(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    img = models.ImageField(upload_to='images/videogames/')
    category = models.CharField(max_length=50)
    launch = models.DateField(blank=True, null=True)
    social_urls = models.ManyToManyField(
        SocialURL,
        related_name="+",
        blank=True,
    )
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    short_name = models.CharField(max_length=10, blank=True, null=True)
    slug = models.SlugField(max_length=40, unique=True)
    img = models.ImageField(upload_to='images/teams/')
    social_urls = models.ManyToManyField(
        SocialURL,
        related_name="+",
        blank=True,
    )
    description = models.TextField()
    videogames = models.ManyToManyField(
        VideoGame,
        related_name='+',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    social_urls = models.ManyToManyField(
        SocialURL,
        related_name="+",
        blank=True,
    )
    team = models.ForeignKey(
        Team,
        related_name='+',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    videogames = models.ManyToManyField(
        VideoGame,
        related_name='+',
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname
