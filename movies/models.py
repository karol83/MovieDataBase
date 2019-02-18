import requests

from django.db import models
from django.utils.translation import gettext as _
from django.contrib.postgres.fields import JSONField
from django.conf import settings


class Ratings(models.Model):
    Source = models.CharField(
        max_length=255,
        verbose_name=_("Rating source"))
    Value = models.CharField(
        max_length=255,
        verbose_name=_("Rating value"))

    def __str__(self):
        return "%s: %s" % (self.Source, self.Value)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    data = JSONField(null=True)

    @staticmethod
    def get_movie_from_api(self, title, max_retries):
        attempt_number = 0
        while attempt_number < max_retries:
            payload = {'apikey': settings.OMDBAPI_KEY, 't': title}
            print('sending request')
            r = requests.get(settings.OMDBAPI_URL, params=payload, timeout=10)
            print('request sent')
            if r.status_code == 200:
                print('request returend with 200')
                data = r.json()
                print(data)

                if data.get('Response') == 'True':
                    movie = Movie.objects.get_or_create(title=data.get('Title'), data=data)
                    print('movie created where movie.data == ')
                    return data
            if r.status_code == 401:
                attempt_number += 1
                print('I cannot login - please check your KEY settings')
            else:
                print('There was a problem with fetching the movie!')
                attempt_number += 1

    movie_added_on_datetime = models.DateTimeField(auto_now_add=True)
    movie_last_accessed_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s" % self.title
