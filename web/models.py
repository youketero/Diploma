from __future__ import unicode_literals
from django.contrib.auth.models import User, Permission
from django.db import models
import datetime


# -- coding: utf-8 --
class type_foto(models.Model):
    header_foto = models.TextField()
    data_foto = models.DateField()
    foto_type = models.TextField(default="enter type of foto here")

    def __str__(self):
        return self.header_foto


class foto_gallery(models.Model):
    foto = models.ImageField(upload_to='web/static/img')
    name_foto = models.TextField(default="name_foto")
    header_id = models.ForeignKey(type_foto, default=1, on_delete=models.CASCADE)
    foto_id = models.IntegerField(default=1)
    def __unicode__(self):
        return "%s %s " % (self.foto_id, self.header_id.header_foto)

class foto_article(models.Model):
    foto = models.ImageField(upload_to="web/static/img")
    foto_id = models.IntegerField(default=1)
    name_foto = models.TextField(max_length=1000, default="enter short description here")

    def __str__(self):
        return "%s %s " % (self.foto_id, self.name_foto)


class Articles(models.Model):
    header_image = models.ManyToManyField(foto_article, default=1)
    title = models.TextField(default="Enter title here")
    image_head = models.ImageField(upload_to="web/static/img", default="#")
    text = models.TextField()
    date = models.DateField()
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return "%s %s " % (self.date, self.header_image)

    def short_text(self):
        if len(self.text) > 100:
            return self.text[:100] + '...'
        else:
            return self.text


class partner(models.Model):
    name = models.TextField()
    short_information = models.TextField()
    foto_logo = models.ImageField(upload_to='web/static/img')
    hyper_link_site = models.TextField(default="http")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s" % (self.name, self.short_information)


class future_conference_anonce(models.Model):
    title = models.CharField(max_length=20000)
    text = models.TextField()
    date = models.DateField()
    location = models.TextField(default="/")
    foto = models.ImageField(upload_to='web/static/img', default="#")
    partner_id = models.ManyToManyField(partner)

    def __str__(self):
        return "%s,%s" % (self.title, self.date)


class structure_staff(models.Model):
    staff_name = models.TextField(default="enter staff here")
    permission_id = models.ForeignKey(Permission, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.staff_name)


class stucture_cathed(models.Model):
    cathed_name = models.TextField(max_length=50)
    cathed_name_rus = models.TextField(max_length=100, default="write")
    history = models.TextField()
    foto = models.ImageField(upload_to='web/static/img')
    number = models.IntegerField(default=0)
    description = models.TextField(default="enter desciption here")
    email = models.TextField(default="http")

    def __str__(self):
        return "%s %s %s" % (self.cathed_name, self.history, self.foto)


class structure_person(models.Model):
    name = models.TextField(default='name')
    last_name = models.TextField(default="sername")
    foto = models.ImageField(upload_to='web/static/img', default="#")
    short_history = models.TextField(default='history')
    cathed_id = models.ForeignKey(stucture_cathed, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(structure_staff, default=1, on_delete=models.CASCADE)
    phone_number = models.IntegerField(default=0)
    monography = models.TextField(default="monography")
    step = models.TextField(default="doctor")

    def __unicode__(self):
        return "%s %s" % (self.name, self.last_name)

    def short_text(self):
        if len(self.short_history) > 100:
            return self.short_history[:100] + '...'
        else:
            return self.short_history

class entrance_specialization(models.Model):
    specialization_name = models.TextField(default="enter specialization here")
    foto = models.ImageField(upload_to='web/static/img', default="#")

    def __str__(self):
        return "%s" % (self.specialization_name)


class entrance_subject(models.Model):
    subject_name = models.TextField(default="enter subject here")
    weigth_coef = models.FloatField(default=0.1)
    min_grade = models.IntegerField(default=1)

    def __str__(self):
        return "%s %s %s" % (self.subject_name, self.min_grade, self.weigth_coef)


class entrance_code(models.Model):
    specialization_code = models.IntegerField(default=103)
    specialization_id = models.ForeignKey(entrance_specialization, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s,%s" % (self.specialization_code, self.specialization_id)








class library_author(models.Model):
    first_name = models.TextField(default="enter first name here")
    last_name = models.TextField(default="enter last name here")

    def __str__(self):
        return "%s,%s" % (self.first_name, self.last_name)


class library_book(models.Model):
    name = models.TextField(default="enter name of the book")
    author_id = models.ManyToManyField(library_author)
    foto = models.ImageField(upload_to='web/static/img', default="#")
    link_for_download = models.FileField(default="enter hyper link here", upload_to="web/static/docs")
    published_in = models.DateField(default=datetime.date.today())
    type_of_book = models.TextField(default="enter type of book")
    user_id = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)


class subject_edu(models.Model):
    subj_name = models.TextField(default="enter name of subject here")
    code = models.TextField(default="OK 1")
    count_credits = models.IntegerField(default="2")
    form_control = models.TextField(default="Іспит")
    cathed_specialization = models.ForeignKey(stucture_cathed, default=1, on_delete=models.CASCADE)



class edu_plan(models.Model):
    choise_cource = ((1, '1'), (2, '2'), (3, '3'),(4,"4"))
    edu_plan_doc = models.FileField(upload_to="web/static/docs")
    cource = models.IntegerField(default=1,choices=choise_cource)

    def __str__(self):
        return "%s" % (self.edu_plan_doc)


class edu_prog(models.Model):
    specialization_id = models.ForeignKey(edu_plan, default=1, on_delete=models.CASCADE)
    subject_edu_id = models.ForeignKey(subject_edu, default=1, on_delete=models.CASCADE)
    language = models.TextField(default="Українська")
    credit_sum = models.IntegerField(default=240)

    def __str__(self):
        return "%s" % (self.specialization_id)


class entrance_specialization_way(models.Model):
    choise_field = (('Бакалавр', 'Бакалавр'), ('Магістр', 'Магістр'), ('Молодший спеціаліст', 'Молодший спеціаліст'))
    code_id = models.ForeignKey(entrance_code, default=1, on_delete=models.CASCADE)
    subject_id = models.ManyToManyField(entrance_subject)
    edu_plan_id = models.ForeignKey(edu_plan, default=1,on_delete=models.CASCADE)
    form_education = models.TextField( choices=choise_field, max_length=1000, default="enter your form of education here")
    education_level = models.TextField(max_length=1000, default="enter your education level here")
    license = models.IntegerField(default=1)
    payment = models.IntegerField(default=1)
    duration_of_study = models.FloatField(default=1.0)
    short_description = models.TextField(max_length=100000,default="Enter description here")

    def __str__(self):
        return "%s,%s" % (self.code_id, self.license)

