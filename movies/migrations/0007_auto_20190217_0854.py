# Generated by Django 2.1.7 on 2019-02-17 07:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_auto_20190215_0218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FavouriteMovie',
            new_name='Movie',
        ),
    ]
