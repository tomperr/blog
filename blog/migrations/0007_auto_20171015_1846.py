# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-15 16:46
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_speedpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speedpost',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.path_and_rename),
        ),
    ]
