from django.urls import path

from .views import (
	wikiIndex,
	gamersIndex, detailGamer, addGamer, editGamer,
	deleteGamer, confirmDeleteGamer, cancelDeleteGamer,
	teamsIndex, detailTeam, addTeam, editTeam,
	videogamesIndex, detailVideoGame, addVideogame, editVideogame,
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),

	path('gamers/', gamersIndex, name="gamersIndex"),
	path('gamer/new/', addGamer, name="addGamer"),
	path('gamer/<slug:slug>', detailGamer, name="detailGamer"),
	path('gamer/edit/<int:pk>', editGamer, name="editGamer"),
	path('gamer/delete/<int:pk>', deleteGamer, name="deleteGamer"),
	path('gamer/delete/confirm/<int:pk>', confirmDeleteGamer, name="confirmDeleteGamer"),
	path('gamer/delete/cancel/<slug:slug>', cancelDeleteGamer, name="cancelDeleteGamer"),

	path('teams/', teamsIndex, name="teamsIndex"),
	path('team/new/', addTeam, name="addTeam"),
	path('team/<slug:slug>/', detailTeam, name="detailTeam"),
	path('team/edit/<int:pk>', editTeam, name="editTeam"),
	
	path('videogames/', videogamesIndex, name="videogamesIndex"),
	path('videogame/new/', addVideogame, name="addVideogame"),
	path('videogame/<slug:slug>/', detailVideoGame, name="detailVideoGame"),
	path('videogame/edit/<int:pk>', editVideogame, name="editVideogame"),
]
