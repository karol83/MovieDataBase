from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required

from .forms import SearchMovieForm, MovieForm
from .models import Movie

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
        data, (movie, _) = movie.get_movie_from_api(
            title=movie_form.cleaned_data['title'],
            max_retries=MAX_RETRIES)
        return render(self.request, 'movie_response.html', {'data': data, 'movie': movie})


class MovieDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'movie'
    queryset = Movie.objects.all()


class FavouriteMoviesList(LoginRequiredMixin, ListView):
    model = Movie
    context_object_name = 'movies'

    def get_queryset(self):
        this_user = self.request.user
        return this_user.movie_set.all()


@login_required()
def add_to_list(request, favourite):
    movie = Movie.objects.get(title=favourite)
    add_to_favourite = movie.favourite_move.add(request.user)
    return render(request, "favourite_added.html")
