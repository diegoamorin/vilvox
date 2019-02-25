from django.contrib import admin

from .models import Tag, List, Post, Profile, socialURL, socialWeb

admin.site.register([Profile, Tag, List, Post, socialURL, socialWeb])
