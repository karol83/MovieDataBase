# Generated by Django 2.1.7 on 2019-02-12 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavouriteMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=255, verbose_name='Movie Title')),
                ('release_year', models.DateField(verbose_name='Movie Relase Year')),
                ('release_date', models.DateTimeField(verbose_name='Movie Release Date')),
                ('runtime', models.PositiveSmallIntegerField(blank=True, verbose_name='Movie Runtime')),
                ('genre', models.CharField(blank=True, max_length=255, verbose_name='Movie Genre')),
                ('director', models.CharField(blank=True, max_length=255, verbose_name='Movie Director')),
                ('actors', models.CharField(blank=True, max_length=255, verbose_name='Actors')),
                ('plot', models.TextField(blank=True, verbose_name='Movie plot')),
                ('language', models.CharField(blank=True, max_length=255, verbose_name='Language')),
                ('country', models.CharField(blank=True, max_length=255, verbose_name='Country')),
                ('awards', models.CharField(blank=True, max_length=255, verbose_name='Awards')),
                ('poster', models.URLField(blank=True, verbose_name='Link to poster URL')),
                ('metascore', models.PositiveSmallIntegerField(blank=True, verbose_name='Metascore')),
                ('imdbRating', models.DecimalField(blank=True, decimal_places=2, max_digits=4, verbose_name='IMDB Rating')),
                ('imdbVotes', models.CharField(blank=True, max_length=15, verbose_name='IMDB Votes')),
                ('imdbID', models.CharField(blank=True, max_length=31, verbose_name='IMDB ID')),
                ('type', models.CharField(blank=True, max_length=50, verbose_name='Type')),
                ('dvd', models.CharField(blank=True, max_length=255, verbose_name='DVD Release Date')),
                ('boxOffice', models.CharField(blank=True, max_length=255, verbose_name='Box office')),
                ('production', models.CharField(blank=True, max_length=255, verbose_name='Production Company')),
                ('website', models.URLField(blank=True, verbose_name='Movie website')),
                ('response', models.BooleanField()),
                ('movie_added_on_datetime', models.DateTimeField(auto_now_add=True)),
                ('movie_last_accessed_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255, verbose_name='Rating source')),
                ('value', models.CharField(max_length=255, verbose_name='Rating value')),
            ],
        ),
        migrations.AddField(
            model_name='favouritemovie',
            name='ratings',
            field=models.ManyToManyField(to='movies.Ratings'),
        ),
    ]
