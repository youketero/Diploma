# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-03-19 18:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20190320_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='foto_id',
            field=models.IntegerField(default=1),
        ),
    ]
