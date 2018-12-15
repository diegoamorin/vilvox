from django.contrib import admin

from .models import Tag, List, Post

admin.site.register([Tag, List, Post])
