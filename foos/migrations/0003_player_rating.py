# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foos', '0002_auto_20170123_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='rating',
            field=models.IntegerField(default=1000),
        ),
    ]
