from django.shortcuts import render, redirect, get_object_or_404

from .models import Team, VideoGame, Gamer
from .forms import TeamForm, VideogameForm, GamerForm

def wikiIndex(request):
	teams_count = Team.objects.all().count()
	videogames_count = VideoGame.objects.all().count()
	gamers_count = Gamer.objects.all().count()

	context = {
		"teams_count": teams_count,
		"videogames_count": videogames_count,
		"gamers_count": gamers_count,
	}
	return render(request, 'wikiIndex.html', context)

# Seccion Gamer

def gamersIndex(request):
	gamers = Gamer.objects.all()
	return render(request, 'gamersIndex.html', {
		'gamers': gamers,
	})

def detailGamer(request, slug):
	gamer = Gamer.objects.get(slug=slug)

	context = {
		"gamer": gamer,
	}
	return render(request, 'detailGamer.html', context)

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

def detailTeam(request, slug):
	team = Team.objects.get(slug=slug)

	context = {
		"team": team,
	}
	return render(request, 'detailTeam.html', context)

# Seccion Videogame

def detailVideoGame(request, slug):
	videogame = VideoGame.objects.get(slug=slug)

	context = {
		"videogame": videogame,
	}
	return render(request, 'detailVideoGame.html', context)

