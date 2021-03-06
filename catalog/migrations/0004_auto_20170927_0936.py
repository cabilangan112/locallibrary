# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-27 01:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_genre_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='name',
        ),
        migrations.RemoveField(
            model_name='genre',
            name='type',
        ),
        migrations.AddField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(default=1, help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=150),
            preserve_default=False,
        ),
    ]
