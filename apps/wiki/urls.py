from django.urls import path

from .views import (
	wikiIndex,
	gamersIndex, detailGamer, addGamer,
	teamsIndex, detailTeam, addTeam,
	detailVideoGame,
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),

	path('gamers/', gamersIndex, name="gamersIndex"),
	path('gamer/new/', addGamer, name="addGamer"),
	path('gamer/<slug:slug>', detailGamer, name="detailGamer"),

	path('teams/', teamsIndex, name="teamsIndex"),
	path('team/new/', addTeam, name="addTeam"),
	path('team/<slug:slug>/', detailTeam, name="detailTeam"),
	
	path('videogame/<slug:slug>/', detailVideoGame, name="detailVideoGame"),
]
