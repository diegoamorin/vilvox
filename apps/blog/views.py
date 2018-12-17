from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Post, Tag, List
from .forms import PostForm, SerieForm, TagForm

def index(request):
	posts = Post.objects.all().order_by('-pk')
	
	query_search = request.GET.get("q")
	if query_search:
		posts = posts.filter(title__icontains=query_search)

	paginator = Paginator(posts, 5) # Show 5 pages per page

	page = request.GET.get('page')
	posts = paginator.get_page(page)

	context = {
		"posts": posts
	}
	return render(request, 'index.html', context)

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
	jumbo = "Editar Articulo"
	post = get_object_or_404(Post, pk=pk)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)

		if form.is_valid():
			form.save()
			return redirect("index")
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

	query_tags = post.tags.values_list()
	tags = []

	for i in range(query_tags.count()):
		tags.append(query_tags[i][1])

	context = {
		"post": post,
		"tags": tags,
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

# Seccion de Etiquetas

def tags(request):
	tags = Tag.objects.all()

	context = {
		"tags": tags
	}
	return render(request, 'tags.html', context)

def detailTag(request, subject):
	tag = Tag.objects.get(subject=subject)

	context = {
		"posts": tag.posts.values,
		"subject": tag.subject,
	}
	return render(request, 'detailTag.html', context)

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

