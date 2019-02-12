from django.db import models
from django.utils.translation import gettext as _
from django.conf import settings


class Ratings(models.Model):
    source = models.CharField(
        max_length=255,
        verbose_name=_("Rating source"))
    value = models.CharField(
        max_length=255,
        verbose_name=_("Rating value"))

    def __str__(self):
        return " ".join(self.source, self.value)


class FavouriteMovie(models.Model):
    movie_title = models.CharField(
        max_length=255,
        verbose_name=_("Movie Title"))
    release_year = models.DateField(
        verbose_name=_("Movie Relase Year"))
    release_date = models.DateTimeField(
        verbose_name=_("Movie Release Date"))
    runtime = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name=_("Movie Runtime"))
    genre = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Movie Genre"))
    director = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Movie Director"))
    actors = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Actors"))
    plot = models.TextField(
        blank=True,
        verbose_name=_("Movie plot"))
    language = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Language"))
    country = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Country"))
    awards = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=('Awards'))
    poster = models.URLField(
        blank=True,
        verbose_name=_("Link to poster URL"))
    ratings = models.ManyToManyField(Ratings)
    metascore = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name=_("Metascore"))
    imdbRating = models.DecimalField(
        blank=True,
        max_digits=4,
        decimal_places=2,
        verbose_name=_("IMDB Rating"))
    imdbVotes = models.CharField(
        blank=True,
        max_length=15,
        verbose_name=_("IMDB Votes"))
    imdbID = models.CharField(
        max_length=31,
        blank=True,
        verbose_name=_("IMDB ID"))
    type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Type"))
    dvd = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("DVD Release Date"))
    boxOffice = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Box office"))
    production = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Production Company"))
    website = models.URLField(
        blank=True,
        verbose_name=_("Movie website"))
    response = models.BooleanField()

    movie_added_on_datetime = models.DateTimeField(auto_now_add=True)
    movie_last_accessed_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return " ".join(self.movie_title, self.release_year)
