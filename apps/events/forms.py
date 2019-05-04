from django import forms

from .models import Event, Game


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'name',
            'short_name',
            'description',
            'start_day',
            'end_day',
            'img',
            'watch_url',
        ]


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'day',
            'videogame',
            'teams',
        ]
