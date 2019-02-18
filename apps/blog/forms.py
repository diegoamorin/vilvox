from django import forms

from .models import Post, List, Tag, CDNImage

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'slug', 'content', 'img', 'series', 'tags']

class SerieForm(forms.ModelForm):
	class Meta:
		model = List
		fields = ['title', 'slug', 'description', 'img']

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['subject']

class CDNImageForm(forms.ModelForm):
	class Meta:
		model = CDNImage
		fields = ['img']
