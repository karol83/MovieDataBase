# Generated by Django 2.1.7 on 2019-02-17 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20190217_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='created_by',
        ),
    ]
