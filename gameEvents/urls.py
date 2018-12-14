from django.urls import path

from .views import eventIndex, eventDetail

urlpatterns = [
	path("events/", eventIndex, name="eventIndex"),
	path("event/<slug:slug>/", eventDetail, name="eventDetail"),
]
