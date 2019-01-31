from django import forms

from .models import Event, Game

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = [
			'name',
			'slug',
			'description',
			'start_day',
			'end_day',
			'img',
		]

class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = [
			'slug',
			'day',
			'videogame',
			'teams',
			'event',
		]
