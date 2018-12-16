from django.shortcuts import render

from .models import Team

def wikiIndex(request):
	
	return render(request, 'wikiIndex.html', {})

def detailTeam(request, slug):
	team = Team.objects.get(slug=slug)

	context = {
		"team": team,
	}
	return render(request, 'detailTeam.html', context)
