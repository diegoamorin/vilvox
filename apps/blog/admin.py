from django.contrib import admin

from .models import Tag, List, Post, Profile, SocialURL, SocialWeb

admin.site.register([Profile, Tag, List, Post, SocialURL, SocialWeb])
