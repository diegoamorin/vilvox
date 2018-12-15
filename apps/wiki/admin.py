from django.contrib import admin

from .models import VideoGame, Team, Gamer

admin.site.register([VideoGame, Team, Gamer])
