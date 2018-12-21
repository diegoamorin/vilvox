from django.urls import path

from .views import eventIndex, eventDetail, addEvent, addGame

urlpatterns = [
	path("events/", eventIndex, name="eventIndex"),
	path("event/new/", addEvent, name="addEvent"),
	path("game/new/<slug:slug>", addGame, name="addGame"),
	path("event/<slug:slug>/", eventDetail, name="eventDetail"),
]
