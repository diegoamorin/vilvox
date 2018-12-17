from django.shortcuts import render

from .models import Team, VideoGame

def wikiIndex(request):
	
	return render(request, 'wikiIndex.html', {})

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
