from django.urls import path

from .views import eventIndex

urlpatterns = [
	path("events/", eventIndex, name="eventIndex")
]