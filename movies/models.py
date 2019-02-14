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
    Title = models.CharField(
        max_length=255,
        verbose_name=_("Movie Title"))
    Year = models.DateField(
        verbose_name=_("Movie Relase Year"))
    Released = models.DateTimeField(
        verbose_name=_("Movie Release Date"))
    Runtime = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_("Movie Runtime"))
    Genre = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Movie Genre"))
    Director = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Movie Director"))
    Actors = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Actors"))
    Plot = models.TextField(
        blank=True,
        verbose_name=_("Movie plot"))
    Language = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Language"))
    Country = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Country"))
    Awards = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=('Awards'))
    Poster = models.URLField(
        blank=True,
        verbose_name=_("Link to poster URL"))
    Ratings = models.ManyToManyField(Ratings)
    Metascore = models.PositiveSmallIntegerField(
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
    Type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name=_("Type"))
    DVD = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("DVD Release Date"))
    BoxOffice = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Box office"))
    Production = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Production Company"))
    Website = models.URLField(
        blank=True,
        verbose_name=_("Movie website"))
    Response = models.BooleanField()

    movie_added_on_datetime = models.DateTimeField(auto_now_add=True)
    movie_last_accessed_datetime = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return " ".join(self.movie_title, self.release_year)
