# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
