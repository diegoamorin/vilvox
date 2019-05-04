from django.urls import path

from .views import (
    eventIndex,
    eventDetail,
    addEvent,
    addGame,
    editGame,
    deleteGame,
    confirmDeleteGame,
    cancelDeleteGame,
)

urlpatterns = [
    path("events/", eventIndex, name="eventIndex"),
    path("event/new/", addEvent, name="addEvent"),
    path("game/new/<slug:slug>/", addGame, name="addGame"),
    path("game/edit/<int:pk>/", editGame, name="editGame"),
    path("game/edit/<slug:slug_event>/<int:pk>", editGame, name="editGame"),
    path("game/delete/<int:pk>/", deleteGame, name="deleteGame"),
    path(
        "game/delete/confirm/<slug:slug>/",
        confirmDeleteGame,
        name="confirmDeleteGame"
    ),
    path(
        "game/delete/cancel/<slug:slug>/",
        cancelDeleteGame,
        name="cancelDeleteGame"
    ),
    path("event/<slug:slug>/", eventDetail, name="eventDetail"),
]
