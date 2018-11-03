from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Tag, List
from .forms import PostForm, SerieForm, TagForm

def index(request):
	posts = Post.objects.all().order_by('-created_at')
	
	posts = {
		"posts": posts, 
	}
	return render(request, 'index.html', posts)

# Seccion de Articulos

@login_required
def addPost(request):
	jumbo = 'Nuevo Articulo'
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect("index")
	else:
		form = PostForm()

	context = {
		"form": form,
		"jumbo": jumbo
	}
	return render(request, "form.html", context)

@login_required
def editPost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	form = PostForm(instance=post)

@login_required
def deletePost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect("index")

# Seccion de Series

def series(request):
	series = List.objects.all()

	series = {
		"series": series,
	}
	return render(request, 'series.html', series)

@login_required
def addSerie(request):
	jumbo = 'Nueva Serie'
	if request.method == 'POST':
		form = SerieForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("series")
	else:
		form = SerieForm()

	context = {
		"form": form,
		"jumbo": jumbo
	}
	return render(request, "form.html", context)

@login_required
def deleteSerie(request, pk):
	serie = get_object_or_404(List, pk=pk)
	serie.delete()
	return redirect('series')

# Seccion de Etiquetas

def tags(request):
	tags = Tag.objects.all()

	tags = {
		"tags": tags,
	}
	return render(request, 'tags.html', tags)

@login_required
def addTag(request):
	jumbo = 'Nueva Etiqueta'
	if request.method == 'POST':
		form = TagForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('tags')

	else:
		form = TagForm()
	
	context = {
		"form": form,
		"jumbo": jumbo
	}
	return render(request, 'form.html', context)

@login_required
def deleteTag(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	tag.delete()
	return redirect("tags")

# Otras Seccciones

def about(request):
	return render(request, 'about.html')

