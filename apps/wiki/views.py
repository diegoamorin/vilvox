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
			return redirect('gamersIndex')
	else:
		form = GamerForm()

	return render(request, "form.html", {
		"form": form,
		"jumbo": jumbo,
	})

@login_required
def editGamer(request, pk):
	jumbo = "Editar Jugador"
	gamer = get_object_or_404(Gamer, pk=pk)

	if request.method == 'POST':
		form = GamerForm(request.POST, request.FILES, instance=gamer)
		if form.is_valid():
			form.save()
			return redirect("detailGamer", slug=gamer.slug)
	else:
		form = GamerForm(instance=gamer)

	return render(request, 'form.html', {
		"form": form,
		"jumbo": jumbo,
	})

@login_required
def deleteGamer(request, pk):
	gamer = get_object_or_404(Gamer, pk=pk)
	return render(request, "confirm_delGamer.html", {
		'gamer': gamer,
	})

@login_required
def confirmDeleteGamer(request, pk):
	gamer = get_object_or_404(Gamer, pk=pk)
	gamer.delete()
	return redirect("gamersIndex")

@login_required
def cancelDeleteGamer(request, slug):
	gamer = get_object_or_404(Gamer, slug=slug)
	return redirect("detailGamer", slug=gamer.slug)

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
			return redirect('teamsIndex')
	else:
		form = TeamForm()

	return render(request, 'form.html', {
		'jumbo': jumbo,
		'form': form,
	})

@login_required
def editTeam(request, pk):
	jumbo = "Editar Team"
	team = get_object_or_404(Team, pk=pk)

	if request.method == 'POST':
		form = TeamForm(request.POST, request.FILES, instance=team)
		if form.is_valid():
			form.save()
			return redirect("detailTeam", slug=team.slug)
	else:
		form = TeamForm(instance=team)

	return render(request, "form.html", {
		"form": form,
		"jumbo": jumbo,
	})

@login_required
def deleteTeam(request, pk):
	team = get_object_or_404(Team, pk=pk)
	return render(request, "confirm_delTeam.html", {
		'team': team,
	})

@login_required
def confirmDeleteTeam(request, pk):
	team = get_object_or_404(Team, pk=pk)
	team.delete()
	return redirect("teamsIndex")

@login_required
def cancelDeleteTeam(request, slug):
	team = get_object_or_404(Team, slug=slug)
	return redirect("detailTeam", slug=team.slug)

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
			return redirect('videogamesIndex')
	else:
		form = VideogameForm()

	return render(request, 'form.html', {
		'jumbo': jumbo,
		'form': form,
	})

@login_required
def editVideogame(request, pk):
	jumbo = "editar Videojuego"
	videogame = get_object_or_404(VideoGame, pk=pk)

	if request.method == 'POST':
		form = VideogameForm(request.POST, request.FILES, instance=videogame)
		if form.is_valid():
			form.save()
			return redirect("detailVideoGame", slug=videogame.slug)
	else:
		form = VideogameForm(instance=videogame)

	return render(request, 'form.html', {
		'form': form,
		'jumbo': jumbo,
	})

@login_required
def deleteVideogame(request, pk):
	videogame = get_object_or_404(VideoGame, pk=pk)
	return render(request, "confirm_delVideogame.html", {
		'videogame': videogame,
	})

@login_required
def confirmDeleteVideogame(request, pk):
	videogame = get_object_or_404(VideoGame, pk=pk)
	videogame.delete()
	return redirect("videogamesIndex")

@login_required
def cancelDeleteVideogame(request, slug):
	videogame = get_object_or_404(VideoGame, slug=slug)
	return redirect("detailVideoGame", slug=videogame.slug)
