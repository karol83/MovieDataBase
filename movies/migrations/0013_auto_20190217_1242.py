# Generated by Django 2.1.7 on 2019-02-17 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20190217_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ratings',
            old_name='source',
            new_name='Source',
        ),
        migrations.RenameField(
            model_name='ratings',
            old_name='value',
            new_name='Value',
        ),
    ]