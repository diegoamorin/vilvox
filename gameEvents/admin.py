from django.contrib import admin

from .models import Event, Game

admin.site.register([Event, Game])
