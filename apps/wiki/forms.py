from django import forms

from .models import VideoGame, Team, Gamer

class VideogameForm(forms.ModelForm):
	class Meta:
		model = VideoGame
		fields = (
			'name', 'slug', 'img', 'category',
			'launch', 'website', 'description'
		)

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = (
			'name', 'slug', 'img', 'website',
			'description', 'videogames'
		)

class GamerForm(forms.ModelForm):
	class Meta:
		model = Gamer
		fields = (
			'nickname', 'slug', 'name', 'birth', 'img',
			'country', 'description', 'country', 'team'
		)
