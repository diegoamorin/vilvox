from django.urls import path

from .views import (
	wikiIndex,
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),
]