# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-07-06 07:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.CharField(max_length=30)),
                ('movie_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=20)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.Movie')),
            ],
        ),
    ]
