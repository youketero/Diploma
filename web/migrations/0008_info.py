# Generated by Django 2.2.8 on 2020-02-07 21:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0007_auto_20200207_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Enter title here')),
                ('image_head', models.ImageField(default='#', upload_to='web/static/img')),
                ('text', models.TextField()),
                ('date', models.DateField()),
                ('link_facebook', models.TextField(default='Enter link here')),
                ('link_telegram', models.TextField(default='Enter link here')),
                ('link_twitter', models.TextField(default='Enter link here')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
