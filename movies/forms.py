from django import forms
from django.utils.translation import gettext as _

from .models import Movie, Ratings


class SearchMovieForm(forms.Form):
    title = forms.CharField(label=_('Movie title'), max_length=255)


class RatingsForm(forms.ModelForm):
    class Meta:
        model = Ratings
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        exclude = ('created_by', 'Ratings')
