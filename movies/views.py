
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator
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
        data, (movie, _) = movie.get_movie_from_api(title=movie_form.cleaned_data['title'], max_retries=MAX_RETRIES)
        print('the movie variable == ', movie)
        return render(self.request, 'movie_response.html', {'data': data, 'movie': movie})


class MovieDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'movie'
    queryset = Movie.objects.all()


@method_decorator(login_required, name='dispatch')
class FavouriteMoviesList(ListView):
    model = Movie
    context_object_name = 'movies'
    # queryset = Movie.objects.all()

    def get_queryset(self):
        this_user = self.request.user
        print('the current user is:', this_user)
        queryset = this_user.movie_set.all()
        print('the questyset is :', queryset)
        return queryset


@login_required()
def add_to_list(request, favourite):
    print('receited the favoutire movie: ', favourite)
    movie = Movie.objects.get(title=favourite)
    add_to_favourite = movie.favourite_move.add(request.user)
    print(add_to_favourite)
    return render(request, "favourite_added.html")
