# Generated by Django 2.1.7 on 2019-02-15 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_auto_20190214_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouritemovie',
            name='Released',
            field=models.DateField(verbose_name='Movie Release Date'),
        ),
        migrations.AlterField(
            model_name='favouritemovie',
            name='Website',
            field=models.URLField(blank=True, null=True, verbose_name='Movie website'),
        ),
        migrations.AlterField(
            model_name='favouritemovie',
            name='Year',
            field=models.CharField(max_length=4, verbose_name='Movie Relase Year'),
        ),
    ]
