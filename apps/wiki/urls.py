from django.urls import path

from .views import (
	wikiIndex,
	gamersIndex, detailGamer, addGamer, editGamer,
	teamsIndex, detailTeam, addTeam,
	videogamesIndex, detailVideoGame, addVideogame
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),

	path('gamers/', gamersIndex, name="gamersIndex"),
	path('gamer/new/', addGamer, name="addGamer"),
	path('gamer/<slug:slug>', detailGamer, name="detailGamer"),

	path('teams/', teamsIndex, name="teamsIndex"),
	path('team/new/', addTeam, name="addTeam"),
	path('team/<slug:slug>/', detailTeam, name="detailTeam"),
	path('team/edit/<int:pk>', editGamer, name="editGamer"),
	
	path('videogames/', videogamesIndex, name="videogamesIndex"),
	path('videogame/new/', addVideogame, name="addVideogame"),
	path('videogame/<slug:slug>/', detailVideoGame, name="detailVideoGame"),
]
