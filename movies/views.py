import requests
import time
from rest_framework import status
from rest_framework.response import Response

from movies.models import FavouriteMovie

from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.conf import settings

from .forms import SearchMovieForm, MovieResult

MAX_RETRIES = 5


def home(request):
    search_form = SearchMovieForm()
    return render(request, "pages/home.html", {'form': search_form})


@method_decorator(login_required, name='dispatch')
class FavouriteMoviesList(ListView):
    model = FavouriteMovie
    context_object_name = 'movies'


@login_required()
def show_movie_details_view(request):
    if request.method == 'POST':
        form = SearchMovieForm(request.POST)
        if form.is_valid():
            payload = {'apikey': settings.OMDBAPI_KEY, 't': form.cleaned_data['title']}
            attempt_num = 0
            while attempt_num < MAX_RETRIES:
                r = requests.get(settings.OMDBAPI_URL, params=payload, timeout=10)
                if r.status_code == 200:
                    data = r.json()
                    if data.get('Response') == 'True':
                        form = MovieResult(initial=data)
                    elif data.get('Response') == 'False':
                        form = ''
                    return render(request, 'movie_response.html', {'data': data, 'form': form})

                else:
                    attempt_num += 1
                    time.sleep(3)
            return Response({"error": "Requests failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
