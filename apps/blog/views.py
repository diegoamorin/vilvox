from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Post, Tag, List
from .forms import PostForm, SerieForm, TagForm

from apps.events.models import Game

def index(request):
	posts = Post.objects.all().order_by('-pk')

	now = timezone.now()
	
	games_index = Game.objects.all().order_by("day")

	games_result = []
	for game in games_index:
		if game.day > now:
			games_result.append(game)

	if len(games_result) >= 5:
		games_five = []
		for game in games_result:
			if len(games_five) < 5:
				games_five.append(game)
	else:
		games_five = []

	""" Seccion Paginacion """
	paginator = Paginator(posts, 8) # Show 8 pages per page
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	""" Fin de Seccion"""

	return render(request, 'index.html', {
		"posts": posts,
		"games_index": games_five,
	})

# Seccion de Articulos

def posts(request):
	posts = Post.objects.all().order_by('-pk')

	query_search = request.GET.get("q")
	if query_search:
		posts = posts.filter(title__icontains=query_search)

	query_tag = request.GET.get("tag")
	if query_tag:
		posts = posts.filter(tags__subject=query_tag)

	paginator = Paginator(posts, 8) # Show 8 pages per page

	page = request.GET.get('page')
	posts = paginator.get_page(page)

	context = {
		"posts": posts
	}
	return render(request, "posts.html", context)

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
	jumbo = "Editar Articulo"
	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)

		if form.is_valid():
			form.save()
			return redirect("detailPost", slug=post.slug)
	else:
		form = PostForm(instance=post)

	context = {
		"form": form,
		"jumbo": jumbo
	}
	return render(request, "form.html", context)

@login_required
def deletePost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	# post.delete()
	context = {
		"post": post
	}
	return render(request, "confirm_delPost.html", context)

@login_required
def confirmDeletePost(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect("index")

@login_required
def cancelDeletePost(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return redirect("detailPost", slug=post.slug)

def detailPost(request, slug):
	post = get_object_or_404(Post, slug=slug)

	recent_post = Post.objects.last()
	if post == recent_post:
		recent_post = None

	query_tags = post.tags.values_list()
	tags = []

	for i in range(query_tags.count()):
		tags.append(query_tags[i][1])

	'''Seccion para articulos relacionados'''
	# Conseguimos las pk de todos los posts
	pks_posts = []
	for i in range(Post.objects.values_list('pk').count()):
		pks_posts.append(Post.objects.values_list('pk')[i][0])

	# Quitamos la pk del post actual para que no se vuelva a repetir
	pks_posts.remove(post.pk)

	# Buscamos que solo nos de 3 posts como max

	''' creamos una lista de [1, ..., numero_tags_el_post]
		y la volteamos [numero_tags_el_post, 1]
		funcionaran como el num de similitudes de max a min que debe de tener 
		el post relacionado para que siempre se llege a tres.
	'''
	num_tags_list = [i for i in range(1, len(tags) + 1)]
	num_tags_reverse = list(reversed(num_tags_list))

	# Buscamos las similitudes
	post_selects = []
	for num_tags in num_tags_reverse:
		for pk in pks_posts:
			# print("Numero de similitudes:", num_tags)
			# print("Post PK:", pk)

			similitudes = 0
			post_tags = get_object_or_404(Post, pk=pk).tags.values_list()

			tag_post_sim = []
			for i in range(post_tags.count()):
				tag_post_sim.append(post_tags[i][1])

			for tag_super in tags:
				if tag_super in tag_post_sim:
					similitudes += 1

			if similitudes == num_tags:
				post_sim = get_object_or_404(Post, pk=pk)
				post_selects.append(post_sim)

			if len(post_selects) == 3:
				break
		if len(post_selects) == 3:
			# print("Pots seleccionados:", post_selects)
			break

	context = {
		"post": post,
		"tags": tags,
		"recent_post": recent_post,
		"post_selects": post_selects,
	}
	return render(request, "detailPost.html", context)

# Seccion de Series

def series(request):
	series = List.objects.all()

	series = {
		"series": series
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
def editSerie(request, pk):
	jumbo = "Editar Serie"
	serie = get_object_or_404(List, pk=pk)

	if request.method == 'POST':
		form = SerieForm(request.POST, request.FILES, instance=serie)

		if form.is_valid():
			form.save()
			return redirect("series")
	else:
		form = SerieForm(instance=serie)

	context = {
		"form": form,
		"jumbo": jumbo,
	}
	return render(request, "form.html", context)

@login_required
def deleteSerie(request, pk):
	serie = get_object_or_404(List, pk=pk)
	context = {
		"serie": serie,
	}
	return render(request, "confirm_delSerie.html", context)

@login_required
def confirmDeleteSerie(request, pk):
	serie = get_object_or_404(List, pk=pk)
	serie.delete()
	return redirect('series')

@login_required
def cancelDeleteSerie(request, slug):
	serie = get_object_or_404(List, slug=slug)
	return redirect('series')

def detailSerie(request, slug):
	serie = get_object_or_404(List, slug=slug)

	context = {
		"serie": serie
	}
	return render(request, "detailSerie.html", context)

# Seccion de Etiquetas

def tags(request):
	tags = Tag.objects.all()

	context = {
		"tags": tags
	}
	return render(request, 'tags.html', context)

@login_required
def editTag(request, subject):
	jumbo = 'Editar Etiqueta'
	tag = get_object_or_404(Tag, subject=subject)
	if request.method == 'POST':
		form = TagForm(request.POST, instance=tag)

		if form.is_valid():
			form.save()
			return redirect('tags')
	else:
		form = TagForm(instance=tag)

	context = {
		"form": form,
		"jumbo": jumbo
	}
	return render(request, 'form.html', context)

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
	return render(request, "form.html", context)

@login_required
def deleteTag(request, pk):
	tag = get_object_or_404(Tag, pk=pk)
	tag.delete()
	return redirect("tags")

# Otras Seccciones

def about(request):
	return render(request, 'about.html')

