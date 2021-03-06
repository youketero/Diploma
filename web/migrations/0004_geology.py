# Generated by Django 2.2.11 on 2020-04-26 19:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200426_0031'),
    ]

    operations = [
        migrations.CreateModel(
            name='Geology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('perimeter', models.FloatField()),
                ('geo4_2l_field', models.IntegerField()),
                ('geo4_2l_id', models.IntegerField()),
                ('glg', models.CharField(max_length=8)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
