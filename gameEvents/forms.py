from django import forms

from .models import Event, Game

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		fields = ['name', 'description', 'start_day', 'end_day', 'img']

class GameForm(forms.ModelForm):
	class Meta:
		model = Game
		fields = ['name', 'day', 'events']
