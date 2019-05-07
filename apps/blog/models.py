from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from markdownx.models import MarkdownxField


class SocialWeb(models.Model):
    name = models.CharField(max_length=20)
    img_icon = models.FileField(upload_to="images/social_icons/")

    def __str__(self):
        return self.name


class SocialURL(models.Model):
    social_web = models.ForeignKey(
        SocialWeb,
        on_delete=models.CASCADE,
        related_name="+",
    )

    url = models.URLField()

    def __str__(self):
        return "%s: %s" % (self.social_web.name, self.url)


class Profile(models.Model):
    # pylint: disable=no-self-use
    # pylint: disable=no-self-argument
    # pylint: disable=unused-argument
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img_perfil = models.ImageField('images/profiles/')
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    social_urls = models.ManyToManyField(
        SocialURL,
        related_name="+",
        blank=True,
    )

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return self.user.username


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
    author = models.ForeignKey(
        Profile,
        related_name='listas',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    img = models.ImageField(upload_to='images/list/')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=120, unique=True)
    author = models.ForeignKey(
        Profile,
        related_name='posts',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )
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
