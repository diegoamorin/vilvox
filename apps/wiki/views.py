from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Team, VideoGame, Gamer
from .forms import TeamForm, VideogameForm, GamerForm

def wikiIndex(request):
	teams_count = Team.objects.all().count()
	videogames_count = VideoGame.objects.all().count()
	gamers_count = Gamer.objects.all().count()

	return render(request, 'wikiIndex.html', {
		"teams_count": teams_count,
		"videogames_count": videogames_count,
		"gamers_count": gamers_count,
	})

# Seccion Gamer

def gamersIndex(request):
	gamers = Gamer.objects.all()
	return render(request, 'gamersIndex.html', {
		'gamers': gamers,
	})

def detailGamer(request, slug):
	gamer = Gamer.objects.get(slug=slug)

	def calculate_age(born):
		today = date.today()
		return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
	edad_gamer = calculate_age(gamer.birth)

	return render(request, 'detailGamer.html', {
		"gamer": gamer,
		"edad_gamer": edad_gamer,
	})

@login_required
def addGamer(request):
	jumbo = 'Nuevo Gamer'
	if request.method == 'POST':
		form = GamerForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = GamerForm()

	return render(request, "form.html", {
		"form": form,
		"jumbo": jumbo,
	})

# Seccion Team

def teamsIndex(request):
	teams = Team.objects.all()
	return render(request, 'teamsIndex.html', {
		'teams': teams,
	})

def detailTeam(request, slug):
	team = Team.objects.get(slug=slug)

	return render(request, 'detailTeam.html', {
		"team": team,
	})

@login_required
def addTeam(request):
	jumbo = 'Agregar Team'
	if request.method == 'POST':
		form = TeamForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = TeamForm()

	return render(request, 'form.html', {
		'jumbo': jumbo,
		'form': form,
	})

# Seccion Videogame

def videogamesIndex(request):
	videogames = VideoGame.objects.all()
	return render(request, 'videogamesIndex.html', {
		'videogames': videogames,
	})

def detailVideoGame(request, slug):
	videogame = VideoGame.objects.get(slug=slug)

	return render(request, 'detailVideoGame.html', {
		"videogame": videogame,
	})

@login_required
def addVideogame(request):
	jumbo = 'Agregar VideoJuego'
	if request.method == 'POST':
		form = VideogameForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = VideogameForm()

	return render(request, 'form.html', {
		'jumbo': jumbo,
		'form': form,
	})
