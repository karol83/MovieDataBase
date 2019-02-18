import requests
import time

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .forms import SearchMovieForm, MovieForm
from .serializers import MovieSerializer, RatingsSerializer
from .models import Movie, Ratings

MAX_RETRIES = 3


def home(request):
    search_form = SearchMovieForm()
    return render(request, "pages/home.html", {'form': search_form})


class FileSearchView(LoginRequiredMixin, FormView):
    template_name = 'pages/home.html'
    form_class = SearchMovieForm
    success_url = '/result/'

    def form_valid(self, movie_form):
        movie = Movie()
        data = movie.get_movie_from_api(movie_form.cleaned_data['title'], MAX_RETRIES)
        return render(self.request, 'movie_response.html', {'data': data})


@method_decorator(login_required, name='dispatch')
class FavouriteMoviesList(ListView):
    model = Movie
    context_object_name = 'movies'


@login_required()
def add_to_list(request):
    data = request.GET.get('data')
    if request.method == 'POST':
        print('the data == ', data)
        form = MovieForm(initial=data)
        print('the form == ', form)
        favourite_movie = form.save(commit=False)
        favourite_movie.Title = data.get('Title')
        favourite_movie.save()
