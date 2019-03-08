from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Event, Game
from .forms import EventForm, GameForm
from ..utils.date_spanish import get_month, get_weekday

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
	gTeams = [list(game.teams.get_queryset()) for game in games]
	gDay = [game.day for game in games]
	gPk = [game.pk for game in games]
	total_games = [
		{'teams':i[0], 'day':i[1], 'pk':i[2]} for i in zip(gTeams, gDay, gPk)
	]

	days_format = []
	for game in total_games:
		day = game.get("day")
		# day_format = Sábado 25 Mayo
		days_format.append(
			get_weekday(day.strftime("%A")) +
			" " + str(day.day) +
			" " + get_month(day.month)
		)

	days_formats_and_games = [
		{"format_day":i[0], "game":i[1]} for i in zip(days_format, total_games)
	]

	days_format_only = []
	for day_format in days_format:
		if not day_format in days_format_only:
			days_format_only.append(day_format)

	date_and_games_full = []
	for day_format in days_format_only:

		games_list = []

		for day_format_and_game in days_formats_and_games:
			if day_format == day_format_and_game.get("format_day"):

				games_list.append(day_format_and_game.get("game"))

		result = {"format_day": day_format, "games": games_list}

		date_and_games_full.append(result)

	return render(request, "detailEvent.html", {
		"event": event,
		"date_and_games_full": date_and_games_full,
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
