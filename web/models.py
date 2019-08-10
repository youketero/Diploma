from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
# -- coding: utf-8 --
class Articles(models.Model):
    image = models.ImageField(upload_to='web/static/img')
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return "%s %s %s"   % (self.date,self.title,self.image)
    def short_text(self):
        if len(self.text)>100:
            return self.text[:100]+'...'
        else:
            return self.text


class anonce(models.Model):
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()






class subject(models.Model):
    subject_name = models.CharField(max_length=10000)

    def __unicode__(self):
        return "%s" %(self.subject_name)


class cathed(models.Model):
    cathed_name = models.TextField(max_length=50)
    cathed_name_rus = models.TextField(max_length=100,default="write")
    history = models.TextField()
    foto = models.ImageField(upload_to='web/static/img')
    number = models.IntegerField(default=0)
    email = models.TextField(default="http")

    def __unicode__(self):
        return "%s %s %s" %(self.cathed_name,self.history, self.foto)

class pare(models.Model):
    id_pare = models.IntegerField(default=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __unicode__(self):
        return "%s %s %s" % (self.id_pare,self.start_time,self.end_time)


class teacher(models.Model):
    name = models.TextField(default='name')
    first_name = models.TextField(default="sername")
    short_history = models.TextField(default='history')
    cathed_id = models.ForeignKey(cathed,on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    monography = models.TextField(default="monography")
    step = models.TextField(default="doctor")

    def __unicode__(self):
        return "%s %s" % (self.name,self.first_name)

class room(models.Model):
    building = models.TextField()
    roof = models.IntegerField(default=301)

    def __unicode__(self):
        return "%s %s" % (self.building,self.roof)

class day(models.Model):
    day = models.TextField()
    def __unicode__(self):
        return self.day

class rozklad(models.Model):
   pare_id = models.ForeignKey(pare,on_delete=models.CASCADE)
   day_id = models.ForeignKey(day,on_delete=models.CASCADE)
   cource = models.IntegerField(default=1)
   subject_id = models.ForeignKey(subject,on_delete=models.CASCADE)
   teacher_id = models.ForeignKey(teacher,on_delete=models.CASCADE)
   room_id = models.ForeignKey(room,on_delete=models.CASCADE)
   cathed_id = models.TextField(default='geology')
   def __unicode__(self):
       return "%s %s %s" % (self.day_id, self.day_id, self.cource)

class type_foto(models.Model):
    header_foto = models.TextField()
    data_foto = models.DateField()

    def __str__(self):
        return  self.header_foto

class gallery(models.Model):
    foto = models.ImageField(upload_to='web/static/img')
    name_foto = models.TextField(default="name_foto")
    header_id = models.ForeignKey(type_foto,default=1,on_delete=models.CASCADE)
    foto_id = models.IntegerField(default=1)



class partner(models.Model):
    name = models.TextField()
    short_information = models.TextField()
    foto_logo = models.ImageField(upload_to='web/static/img')
    hyper_link_site = models.TextField(default="http")

class hyper_link_usefull(models.Model):
    name = models.TextField()
    type = models.TextField()
    hyper_link = models.TextField()