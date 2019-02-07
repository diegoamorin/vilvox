from django.urls import path

from .views import (
	eventIndex, eventDetail, addEvent, addGame,
	editGame
)

urlpatterns = [
	path("events/", eventIndex, name="eventIndex"),
	path("event/new/", addEvent, name="addEvent"),
	path("game/new/<slug:slug>", addGame, name="addGame"),
	path("game/edit/<int:pk>", editGame, name="editGame"),
	path("event/<slug:slug>/", eventDetail, name="eventDetail"),
]
