from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

class Articles(models.Model):
    image = models.ImageField(upload_to='web/static/img')
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return "%s %s %s"  % (self.date,self.title,self.image)

class anonce(models.Model):
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User)
