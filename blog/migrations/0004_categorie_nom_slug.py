# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-25 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='nom_slug',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
