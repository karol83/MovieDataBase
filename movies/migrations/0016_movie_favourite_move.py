# Generated by Django 2.1.7 on 2019-02-19 20:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0015_delete_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='favourite_move',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
