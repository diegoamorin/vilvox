from django.urls import path

from .views import eventIndex, eventDetail, addEvent

urlpatterns = [
	path("events/", eventIndex, name="eventIndex"),
	path("event/new/", addEvent, name="addEvent"),
	path("event/<slug:slug>/", eventDetail, name="eventDetail"),
]
