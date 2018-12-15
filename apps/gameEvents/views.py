from django.shortcuts import render

from .models import Event, Game
from .forms import EventForm, GameForm

def eventIndex(request):
	events = Event.objects.all()

	context = {
		"events": events,
	}
	return render(request, "events_templates/event_index.html", context)

def eventDetail(request, slug):
	event = Event.objects.get(slug=slug)
	games = Event.objects.get(slug=slug).games.get_queryset()

	context = {
		"event": event,
		"games": games,
	}
	return render(request, "events_templates/detailEvent.html", context)
