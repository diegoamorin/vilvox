from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Event, Game
from .forms import EventForm, GameForm

def eventIndex(request):
	events = Event.objects.all()

	return render(request, "event_index.html", {
		"events": events,
	})

def eventDetail(request, slug):
	event = get_object_or_404(Event, slug=slug)
	games = (
		get_object_or_404(Event, slug=slug)
		.games
		.get_queryset()
		.order_by('day')
	)
	lista = [list(game.teams.get_queryset()) for game in games]
	lista2 = [game.day for game in games]
	lista3 = [game.pk for game in games]
	lista_total = [
		{'teams':i[0], 'day':i[1], 'pk':i[2]} for i in zip(lista, lista2, lista3)
	]
	return render(request, "detailEvent.html", {
		"event": event,
		"games": lista_total,
	})

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

	return render(request, "form.html", {
		"form": form,
		"jumbo": jumbo,
	})

@login_required
def addGame(request, slug):
	jumbo = 'Nuevo Juego'
	event = get_object_or_404(Event, slug=slug)

	if request.method == 'POST':
		form = GameForm(request.POST, request.FILES)
		if form.is_valid():
			game = form.save(commit=False)
			game.event = event
			game.save()
			form.save_m2m()
			return redirect('eventDetail', slug=event.slug)
	else:
		form = GameForm()

	return render(request, "form.html", {
		"form": form,
		"jumbo": jumbo,
	})

@login_required
def editGame(request, pk, slug_event):
	jumbo = "Editar Juego"
	game = get_object_or_404(Game, pk=pk)

	if request.method == 'POST':
		form = GameForm(request.POST, request.FILES, instance=game)

		if form.is_valid():
			form.save()
			return redirect("eventDetail", slug=slug_event)
	else:
		form = GameForm(instance=game)

	return render(request, 'form.html',{
		'jumbo':jumbo,
		'form': form,
	})

@login_required
def deleteGame(request, pk):
	game = get_object_or_404(Game, pk=pk)
	return render(request, "confirm_delGame.html", {
		"game": game,
	})

@login_required
def confirmDeleteGame(request, slug):
	game = get_object_or_404(Game, slug=slug)
	game.delete()
	return redirect("eventIndex")

@login_required
def cancelDeleteGame(request, slug):
	game = get_object_or_404(Game, slug=slug)
	event = Event.objects.filter(games__slug=game.slug)
	return redirect("eventDetail", slug=event[0].slug)
