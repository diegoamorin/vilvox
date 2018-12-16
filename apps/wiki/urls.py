from django.urls import path

from .views import (
	wikiIndex, detailTeam,
)

urlpatterns = [
	path('', wikiIndex, name="wikiIndex"),
	path('team/<slug:slug>/', detailTeam, name="detailTeam"),
]
