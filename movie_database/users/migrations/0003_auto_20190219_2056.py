# Generated by Django 2.1.7 on 2019-02-19 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_favourite_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='favourite_movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]
