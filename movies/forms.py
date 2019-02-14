from django import forms
from django.utils.translation import gettext as _

from .models import FavouriteMovie


class SearchMovieForm(forms.Form):
    title = forms.CharField(label=_('Movie title'), max_length=255)


class MovieResult(forms.ModelForm):
    class Meta:
        model = FavouriteMovie
        exclude = ('created_by',)
