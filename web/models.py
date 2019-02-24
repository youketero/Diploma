from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# -- coding: utf-8 --
class Articles(models.Model):
    image = models.ImageField(upload_to='web/static/img')
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return "%s %s %s"   % (self.date,self.title,self.image)
    def short_text(self):
        if self.text>100:
            return self.text[:100]+'...'
        else:
            return self.text
class anonce(models.Model):
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    user = models.ForeignKey(User)





class subject(models.Model):
    subject_name = models.CharField(max_length=10000)

    def __unicode__(self):
        return "%s" %(self.subject_name)

class cource(models.Model):
    cathed_name = models.TextField(max_length=50)
    cource_id = models.IntegerField()

    def __unicode__(self):
        return "%s %s" %(self.cathed_name,self.cource_id)

class pare(models.Model):
    id_pare = models.IntegerField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return "%s %s %s" % (self.id_pare,self.start_time,self.end_time)

class teacher(models.Model):
    name = models.TextField()
    first_name = models.TextField()

    def __unicode__(self):
        return "%s %s" % (self.name,self.first_name)

class room(models.Model):
    building = models.TextField()
    roof = models.IntegerField()

    def __unicode__(self):
        return "%s %s" % (self.building,self.roof)

class day(models.Model):
    day = models.TextField()

    def __unicode__(self):
        return self.day

class rozklad(models.Model):
   pare_id = models.ForeignKey(pare)
   day_id = models.ForeignKey(day)
   cource_id = models.ForeignKey(cource)
   cource = models.IntegerField(default=1)
   subject_id = models.ForeignKey(subject)
   teacher_id = models.ForeignKey(teacher)
   room_id = models.ForeignKey(room)

   def __unicode__(self):
       return "%s %s %s" % (self.day_id, self.day_id, self.cource_id)
