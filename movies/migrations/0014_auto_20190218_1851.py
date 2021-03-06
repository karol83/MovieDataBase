# Generated by Django 2.1.7 on 2019-02-18 17:51

import datetime
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20190217_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='Actors',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Awards',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='BoxOffice',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='DVD',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Metascore',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Plot',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Poster',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Production',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Ratings',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Released',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Response',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Runtime',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Title',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Type',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Website',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbID',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbRating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='imdbVotes',
        ),
        migrations.AddField(
            model_name='movie',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default=datetime.datetime(2019, 2, 18, 17, 51, 2, 271117, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
