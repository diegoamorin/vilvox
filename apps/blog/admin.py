from django.contrib import admin

from .models import Tag, List, Post, Profile

admin.site.register([Profile, Tag, List, Post])
