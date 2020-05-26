import q as q
from django.contrib.gis.db.models.functions import AsGeoJSON
from django.core.files.storage import FileSystemStorage
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.
from django.views.generic import ListView, TemplateView
from django.contrib.postgres.search import SearchVector
from django.views import View

from web.forms import  DocumentForm
from web.gis_data import run, run_shape
from web.models import Articles, future_conference_anonce, entrance_specialization_way, \
    partner, type_foto, foto_article, foto_gallery, stucture_cathed, library_book, structure_person, edu_plan, \
    entrance_subject, Info, pointX, Points, Points_city, Geology
from photologue.models import *
import zipfile






def home(request):
    articles = Articles.objects.order_by('id').reverse()[:8]
    foto_galery = Gallery.objects.all()
    partners = partner.objects.all()
    future_conference_anonce_full = future_conference_anonce.objects.all()
    sub = entrance_specialization_way.objects.all()
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'web/home.html', locals())


def vstup(request):
    sub = entrance_specialization_way.objects.all()
    return render(request, "web/vstup.html", locals())


def vstup_info(request, id):
    vs = get_object_or_404(entrance_specialization_way, code_id__specialization_id__specialization_name=id)
    # sub = entrance_subject.objects.filter(specialization_code__specialization_id__specialization_name = id)
    sub1 = entrance_specialization_way.objects.all()
    return render(request, "web/vstup_info.html", locals())


def partneru(request):
    partner_each = partner.objects.all()
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'web/partner.html', locals())


def news(request):
    articles = Articles.objects.order_by('id').reverse()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "web/news.html", locals())


def show_articles(request, article_title):
    article = get_object_or_404(Articles, title=article_title)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'web/article.html', locals())


def library(request):
    books = library_book.objects.all()
    articles = Articles.objects.order_by('id').reverse()
    return render(request, "web/library.html", locals())


def galery(request):
    gallery1 = Gallery.objects.all()
    return render(request, "web/gallery.html", locals())


def show_galery(request, header_foto):
    show_galery = Photo.objects.filter(title__startswith=header_foto)
    return render(request, 'web/galery_type.html', locals())


def anonce1(request):
    future_conference_anonce_full = future_conference_anonce.objects.all()
    return render(request, 'web/anonce.html', locals())



def anonce_detail(request, anonce_id):
    anonce_details = get_object_or_404(future_conference_anonce, id=anonce_id)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, 'web/anonce_detail.html', locals())


def contact(request):
    return render(request, "web/contact.html", locals())


def about(request):
    return render(request, "web/about.html", locals())


def structure(request):
    cathed2 = stucture_cathed.objects.all()
    return render(request, "web/structure.html", locals())


def cathed_b(request, cathed_name):
    cathed_each = get_object_or_404(stucture_cathed, cathed_name=cathed_name)
    teacher1 = structure_person.objects.filter(cathed_id__cathed_name=cathed_name)
    return render(request, "web/cathed.html", locals())

def teacher(request, teacher):
    teacher = get_object_or_404(structure_person, id=teacher)
    return render(request, "web/teacher_info.html", locals())

def info(request):
    all_article = Articles.objects.order_by("id").reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "web/Information.html", locals())

def edu_plans(request):
    sub = entrance_specialization_way.objects.all()
    return render(request, "web/edu_plan.html", locals())


def education(request):
    return render(request, "web/education.html", locals())


class search(View):

    def get(self, request, *args, **kwargs):

        query = self.request.GET.get('q')
        if query is not None:
            query = self.request.GET.get('q')
            if query:
                articles = Articles.objects.annotate(search=SearchVector('title')).filter(search=query)
                partners = partner.objects.annotate(search=SearchVector('name')).filter(search=query)
                teachers = structure_person.objects.annotate(search=SearchVector('name', 'last_name')).filter(
                    search=query)
        return render(request, "web/search_results.html", locals())


def handler404(request, exception, template_name="web/page404.html"):
    response = render_to_response("web/page404.html")
    response.status_code = 404
    return response


def science_learning(request):
    return render(request, "web/science_learning.html", locals())


def phd_learning(request):
    return render(request, 'web/phd_learning.html', locals())


def info_for_students(request):
    info_for_student = Info.objects.order_by('id').reverse()
    paginator = Paginator(info_for_student, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "web/info_for_students.html", locals())


def info_detailed(request, info_title):
    info_for_student = get_object_or_404(Info, title=info_title)
    all_article = Articles.objects.order_by('id').reverse()[:8]
    info = Info.objects.order_by("id").reverse()[:8]
    return render(request, "web/info_for_students_detail.html", locals())

def Gis_page(request):
    folder = 'web\static\gis_data'
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.FILES["file"]
            form.save()
            fs = FileSystemStorage(location=folder)
            with zipfile.ZipFile(fs.location+"\\"+str(name), 'r') as zip_ref:
                zip_ref.extractall(fs.location)
            run(str(name)[0:-4])
            os.remove(fs.location + "\\" + str(name))
        return render(request, "web/gis_page.html", locals())
    else:
        form = DocumentForm()
        return render(request,"web/gis_page.html",locals())


def Gis_page1(request):
    folder = 'web\static\gis_data'
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            name = request.FILES["file"]
            form.save()
            fs = FileSystemStorage(location=folder)
            with zipfile.ZipFile(fs.location+"\\"+str(name), 'r') as zip_ref:
                zip_ref.extractall(fs.location)
            run(str(name)[0:-4])
            os.remove(fs.location + "\\" + str(name))
        return render(request, "web/gis_page.html", locals())
    else:
        form = DocumentForm()
        return render(request,"web/gis_page.html",locals())


def gis_points(request):
    gis_data = serialize("geojson",Points.objects.all())
    return HttpResponse(gis_data,content_type="json")

def gis_city(request):
    gis_data = serialize("geojson",Points_city.objects.all())
    return HttpResponse(gis_data,content_type="json")

def geol(request):
    geol_data = serialize("geojson",Geology.objects.all())
    return HttpResponse(geol_data,content_type="json")