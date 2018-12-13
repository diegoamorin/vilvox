from django.shortcuts import render

from .models import Event, Game
from .forms import EventForm, GameForm

def eventIndex(request):
	events = Event.objects.all()

	context = {
		"events": events,
	}
	
	return render(request, "events_templates/event_index.html", context)
