from django.urls import path

from .views import (
	wikiIndex,
	detailTeam, detailVideoGame, detailGamer,
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),
	path('team/<slug:slug>/', detailTeam, name="detailTeam"),
	path('videogame/<slug:slug>/', detailVideoGame, name="detailVideoGame"),
	path('gamer/<slug:slug>', detailGamer, name="detailGamer"),
]
