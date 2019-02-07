from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Event, Game
from .forms import EventForm, GameForm

def eventIndex(request):
	events = Event.objects.all()

	context = {
		"events": events,
	}
	return render(request, "event_index.html", context)

def eventDetail(request, slug):
	event = get_object_or_404(Event, slug=slug)
	games = get_object_or_404(Event, slug=slug).games.get_queryset()

	lista = [list(game.teams.get_queryset()) for game in games]
	lista2 = [game.day for game in games]
	lista3 = [game.pk for game in games]
	lista_total = [
		{'teams':i[0], 'day':i[1], 'pk':i[2]} for i in zip(lista, lista2, lista3)
	]

	context = {
		"event": event,
		"games": lista_total,
	}
	return render(request, "detailEvent.html", context)

@login_required
def addEvent(request):
	jumbo = 'Nuevo Evento'
	if request.method == 'POST':
		form = EventForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("eventIndex")
	else:
		form = EventForm()

	context = {
		"form": form,
		"jumbo": jumbo,
	}
	return render(request, "form.html", context)

@login_required
def addGame(request, slug):
	jumbo = 'Nuevo Juego'
	event = get_object_or_404(Event, slug=slug)

	if request.method == 'POST':
		form = GameForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('eventDetail', slug=event.slug)
	else:
		form = GameForm()

	context = {
		"form": form,
		"jumbo": jumbo,
	}
	return render(request, "form.html", context)

@login_required
def editGame(request, pk):
	jumbo = "Editar Juego"
	game = get_object_or_404(Game, pk=pk)
	event = Event.objects.filter(games__slug=game.slug)

	if request.method == 'POST':
		form = GameForm(request.POST, request.FILES, instance=game)

		if form.is_valid():
			form.save()
			return redirect("eventDetail", slug=event[0].slug)
	else:
		form = GameForm(instance=game)

	return render(request, 'form.html',{
		'jumbo':jumbo,
		'form': form,
	})
