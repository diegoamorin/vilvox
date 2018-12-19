from django.shortcuts import render

from .models import Team, VideoGame, Gamer

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

def detailTeam(request, slug):
	team = Team.objects.get(slug=slug)

	context = {
		"team": team,
	}
	return render(request, 'detailTeam.html', context)

def detailVideoGame(request, slug):
	videogame = VideoGame.objects.get(slug=slug)

	context = {
		"videogame": videogame,
	}
	return render(request, 'detailVideoGame.html', context)

def detailGamer(request, slug):
	gamer = Gamer.objects.get(slug=slug)

	context = {
		"gamer": gamer,
	}
	return render(request, 'detailGamer.html', context)
