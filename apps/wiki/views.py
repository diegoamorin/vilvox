from django.shortcuts import render

def wikiIndex(request):
	
	return render(request, 'wikiIndex.html', {})
