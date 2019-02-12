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


def home(request):
    context = {}
    return render(request, "pages/home.html", context)


@method_decorator(login_required, name='dispatch')
class FavouriteMoviesList(ListView):
    model = FavouriteMovie
    context_object_name = 'movies'


MAX_RETRIES = 5


# @method_decorator(login_required, name='dispatch')
def omdbapi_api_view(request, title=None):

    payload = {'apikey': settings.OMDBAPI_KEY, 't': title}

    if request.method == 'GET':
        attempt_num = 0
        while attempt_num < MAX_RETRIES:
            r = requests.get(settings.OMDBAPI_URL, params=payload, timeout=10)

            if r.status_code == 200:
                data = r.json()
                print('the response data == ', data)
                return Response(data, status=status.HTTP_200_OK)
            else:
                attempt_num += 1
                time.sleep(3)
        return Response({"error": "Requests failed"}, status=r.status_code)
    else:
        return Response({"error": "Method not allowed"}, status=status.HTTP_400_BAD_REQUEST)
