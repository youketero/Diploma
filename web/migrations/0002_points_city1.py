# Generated by Django 2.2.11 on 2020-04-25 19:28

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points_city1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_city', models.ImageField(default='#', upload_to='web/static/img')),
                ('city_name', models.CharField(max_length=40)),
                ('admin_name', models.CharField(max_length=42)),
                ('cntry_name', models.CharField(max_length=40)),
                ('status', models.CharField(max_length=50)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=3857)),
            ],
        ),
    ]
